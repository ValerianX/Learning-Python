class File:
    def __init__(self, file_name: str, index: int, sample_length_ms: int, sample_length_samples: int = None):
        self.file_name = file_name
        self.index = index
        self.sample_length_ms = sample_length_ms
        self.sample_rate = 12000
        if sample_length_samples is None:
            self.sample_length_samples = int(self.sample_length_ms/1000*self.sample_rate)
        else:
            self.sample_length_samples = sample_length_samples
            self.sample_length_ms = int(sample_length_samples/self.sample_rate*1000)
        self.measurement_ids = self._get_measurement_ids()

    def __len__(self):
        return len(self.measurement_ids)

    def _get_measurement_ids(self):
        try:
            file = os.path.split(self.file_name)[-1].replace(".mat", "")
            total_samples = len(loadmat(self.file_name, simplify_cells=True)["X"+file.split("_")[-1]+"_DE_time"])
            number_splits = int(total_samples//self.sample_length_samples)
            return range(number_splits)
        except TypeError as e:
            print("Failed to load .mat file: \"{}\". Maybe the file is corrupted.".format(self.file_name))
            raise e

    def get_index_list(self):
        indexes = [(self.index, i) for i in self.measurement_ids]
        return indexes
      
      
      
      
      
      ## second snippet

    @staticmethod
    def _labels() -> dict:
        modes = {"0HP": 0, "1HP": 1, "2HP": 2, "3HP": 3}
        faults = {"K0": 0, "KA": 1, "KB": 2, "KI": 3}
        severities = {"00": 0, "07": 1, "14": 2, "21": 3}
        return {"modes": modes, "faults": faults, "severities": severities}

    def _read_label(self, path: str):
        """Method that reads the label for a measurement file saved under path.

                Args:
                    path (str): path to measurement

                Returns:
                    numpy array with encoded labels as numbers
                """

        splitted_path = os.path.split(path)
        mode = splitted_path[1][:3]
        fault = os.path.split(path)[0][-2:]
        severity = splitted_path[1][4:6]
        label_code = self.labels["modes"][mode] * self.labels["faults"][fault] * self.labels["severities"][severity]
        return label_code
      
      
      
what is a static method ?
what is a class method ?
what is abstract method ?


how to create a child class from a parent class ?...


what are dunder methods in python ?

what is self.__variablename ? and how double underscore variable different from single underscore and without underscore variable name ?
      
      
      
      
      
      
