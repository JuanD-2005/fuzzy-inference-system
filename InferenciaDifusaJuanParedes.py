import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
import matplotlib.pyplot as plt

print("--- INICIANDO SISTEMA DE INFERENCIA DIFUSA ---")


#1 DEFINICIÓN DE VARIABLES (COMÚN)

# Temperatura: [25, 70]
temperatura = ctrl.Antecedent(np.arange(25, 71, 1), 'temperatura')
# Velocidad Proc: [1.2, 3.2]
velocidad = ctrl.Antecedent(np.arange(1.2, 3.3, 0.1), 'velocidad')
# Actividad Disco: [0, 100]
actividad = ctrl.Antecedent(np.arange(0, 101, 1), 'actividad')
# Salida Ventilador: [0, 1]
ventilador = ctrl.Consequent(np.arange(0, 1.1, 0.1), 'ventilador')


#2 FUNCIONES DE MEMBRESÍA (TRAPEZOIDALES)


# --- Temperatura ---
temperatura['T1'] = fuzz.trapmf(temperatura.universe, [4.75, 22.75, 27.25, 45.25])
temperatura['T2'] = fuzz.trapmf(temperatura.universe, [27.25, 45.25, 49.75, 67.75])
temperatura['T3'] = fuzz.trapmf(temperatura.universe, [49.75, 67.75, 72.25, 90.25])

# --- Velocidad ---
velocidad['V1'] = fuzz.trapmf(velocidad.universe, [0.3, 1.1, 1.3, 2.1])
velocidad['V2'] = fuzz.trapmf(velocidad.universe, [1.3, 2.1, 2.3, 3.1])
velocidad['V3'] = fuzz.trapmf(velocidad.universe, [2.3, 3.1, 3.3, 4.1])

# --- Actividad ---
actividad['A1'] = fuzz.trapmf(actividad.universe, [-45, -5, 5, 45])
actividad['A2'] = fuzz.trapmf(actividad.universe, [5, 45, 55, 95])
actividad['A3'] = fuzz.trapmf(actividad.universe, [55, 95, 105, 145])

# --- Ventilador (Salida) ---
ventilador['OFF'] = fuzz.trapmf(ventilador.universe, [-0.9, -0.1, 0.1, 0.9])
ventilador['ON'] = fuzz.trapmf(ventilador.universe, [0.1, 0.9, 1.1, 1.9])


#3 SISTEMA ORIGINAL

print("\n--- EJECUTANDO SISTEMA ORIGINAL ---")


# Regla 1: 1 1 1, 1 (AND) -> Si T1 y V1 y A1 entonces OFF
rule1 = ctrl.Rule(temperatura['T1'] & velocidad['V1'] & actividad['A1'], ventilador['OFF'])

# Regla 2: 3 3 3, 2 (OR, según nota :2) -> Si T3 o V3 o A3 entonces ON
rule2 = ctrl.Rule(temperatura['T3'] | velocidad['V3'] | actividad['A3'], ventilador['ON'])

# Regla 3: 2 2 2, 2 (AND, según nota :1) -> Si T2 y V2 y A2 entonces ON
rule3 = ctrl.Rule(temperatura['T2'] & velocidad['V2'] & actividad['A2'], ventilador['ON'])

# Crear Sistema de Control Original
sistema_orig = ctrl.ControlSystem([rule1, rule2, rule3])
simulacion_orig = ctrl.ControlSystemSimulation(sistema_orig)

# Entradas de prueba (Valores arbitrarios para poner a prueba el sistema)

input_temp = 55
input_vel = 2.5
input_act = 60

simulacion_orig.input['temperatura'] = input_temp
simulacion_orig.input['velocidad'] = input_vel
simulacion_orig.input['actividad'] = input_act

try:
    simulacion_orig.compute()
    resultado_orig = simulacion_orig.output['ventilador']
    print(f"Entradas: Temp={input_temp}, Vel={input_vel}, Act={input_act}")
    print(f"Salida Ventilador (Original): {resultado_orig:.4f}")
    
    # Visualizar
    ventilador.view(sim=simulacion_orig)
    plt.title("Resultado Sistema Original")
    plt.show()
except Exception as e:
    print(f"Error en sistema original: {e}")



#4 SISTEMA MODIFICADO

print("\n--- EJECUTANDO SISTEMA MODIFICADO ---")
print("Modificación: Se cambia la Regla 3 para que sea más sensible (usando OR en vez de AND).")


# Nueva Regla 3: Si T2 O V2 O A2 entonces ON (Antes era Y)
rule3_mod = ctrl.Rule(temperatura['T2'] | velocidad['V2'] | actividad['A2'], ventilador['ON'])

# IMPORTANTE: Creamos un NUEVO sistema con la regla modificada
sistema_mod = ctrl.ControlSystem([rule1, rule2, rule3_mod])
simulacion_mod = ctrl.ControlSystemSimulation(sistema_mod)

# Usamos las MISMAS entradas para poder comparar justamente
simulacion_mod.input['temperatura'] = input_temp
simulacion_mod.input['velocidad'] = input_vel
simulacion_mod.input['actividad'] = input_act

try:
    simulacion_mod.compute()
    resultado_mod = simulacion_mod.output['ventilador']
    print(f"Salida Ventilador (Modificado): {resultado_mod:.4f}")
    
    # Visualizar comparación
    ventilador.view(sim=simulacion_mod)
    plt.title("Resultado Sistema Modificado (Regla 3 con OR)")
    plt.show()
except Exception as e:
    print(f"Error en sistema modificado: {e}")

print("\n--- FIN DEL PROCESO ---")