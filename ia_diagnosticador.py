import google.generativeai as genai

class AsistenteMecanicoIA:
    def __init__(self, api_key):
        """
        Constructor de la clase. Inicializa la conexión con Google Gemini
        utilizando el modelo exacto que requiere el servidor.
        """
        # 1. Le pasamos la llave a la librería oficial
        genai.configure(api_key=api_key)
        
        # 2. Definimos explícitamente el modelo que nos pidió Google en el error
        modelo_elegido = 'gemini-3.6-flash'
        
        # 3. Configuramos la IA
        self.modelo = genai.GenerativeModel(modelo_elegido)

    def diagnosticar_codigo(self, vehiculo, codigo_obd2):
        """
        Método que arma el prompt inteligente y se lo manda a la IA
        para que devuelva el diagnóstico técnico del vehículo.
        """
        prompt = f"""
        Actúa como un inyeccionista automotriz experto y diagnosticador avanzado.
        El vehículo es un: {vehiculo}.
        El escáner arrojó el código de falla o síntoma: {codigo_obd2}.
        
        Por favor, devolveme la respuesta con esta estructura clara y sin introducciones largas:
        1. Significado corto de la falla.
        2. Las 3 causas más comunes (sensores, cableado, etc.).
        3. Qué debe revisar el mecánico físicamente en el auto con un multímetro o herramientas básicas.
        """
        
        try:
            # Hacemos la llamada a la IA de Google
            respuesta = self.modelo.generate_content(prompt)
            return respuesta.text
        except Exception as e:
            # Si llega a haber algún problema técnico, lo atrapamos acá
            return f"Error técnico de la IA: {e}"