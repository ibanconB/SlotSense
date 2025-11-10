class Step:
    """
        Clase base para los Steps del engine
        cada step recibe un SpinContext
    """

    name = "abstract-step"

    def run(self, context):
        raise NotImplementedError(f"{self.__class__.__name__} debe implementar run()")