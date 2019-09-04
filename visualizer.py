from pprint import pprint


class NotExistLayerError(Exception):
    def __init__(self, mes):
        super(NotExistLayerError, self).__init__(mes)


class Visualizer:
    def __init__(self, model):
        self.__model = model
        self.__layer = {}

    def separate_layers(self):
        for i, layer in enumerate(self.__model.named_modules()):
            if i == 0:
                continue

            self.__layer[layer[0]] = layer[1]

    def describe_layers(self):
        """ describe each layer's information
        """
        pprint(self.__layer)

    def check_output(self, layer_name, inputs):
        if not layer_name in self.__layer.keys():
            raise NotExistLayerError(f"You specify not existed layer name: {layer_name}")

        output = self.__layer[layer_name](inputs)
        return output
