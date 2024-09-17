import pandas as pd
import pyttsx3

# Supongamos que tienes un DataFrame con las conversaciones
conversations_df = pd.DataFrame({
    'Usuario': ['Alice', 'Bob', 'Alice', 'Bob'],
    'Mensaje': ['Hola, ¿cómo estás?', '¡Bien, gracias! ¿Y tú?', 'Muy bien también.', 'Me alegro.'],
})

# Convertir las conversaciones en texto concatenado por usuario
conversations_text = conversations_df.groupby('Usuario')['Mensaje'].apply(lambda x: ' '.join(x)).reset_index()

# Inicializar el motor de síntesis de voz
engine = pyttsx3.init()

# Configurar la velocidad de la voz (opcional)
engine.setProperty('rate', 150)

# Iterar sobre cada conversación y convertirla a audio
for index, row in conversations_text.iterrows():
    usuario = row['Usuario']
    mensaje = row['Mensaje']
    
    # Imprimir la conversación en la consola (opcional)
    print(f"{usuario}: {mensaje}")
    
    # Convertir el texto a voz y guardarlo en un archivo de audio
    engine.save_to_file(mensaje, f"{usuario}_conversacion.mp3")

# Cerrar el motor de síntesis de voz
engine.runAndWait()