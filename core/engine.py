class BaseEngine:
    """Engine base que orquesta la ejecucion de Steps."""

    def __init__(self, steps: list):
        # Lista de steps
        self.steps = steps


    def spin(self,  context, as_json=False):
        """Ejecuta cada Step en orden, pasando el mismo contexto"""

        for step in self.steps:
            step.run(context)

        #Despues de ejecutar los Steps, tenemos el resultado
        context.payout = context.total_win

        return context.to_json() if as_json else context.to_dict()
