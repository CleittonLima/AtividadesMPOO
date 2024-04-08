class TV:
    def __init__(self, brand, size, resolution, framerate):
        self.power = False
        self.channel = 1
        self.volume = 5
        self.mute = False
        self.brand = brand
        self.size = size
        self.resolution = resolution
        self.framerate = framerate

    def toggle_power(self):
        self.power = not self.power
        if self.power:
            print("TV ligada")
        else:
            print("TV desligada")

    def change_channel(self, channel):
        if self.power:
            self.channel = channel
            print("Canal alterado para", self.channel)
        else:
            print("Por favor, ligue a TV primeiro")

    def increase_volume(self):
        if self.power:
            if self.volume < 10:
                self.volume += 1
                print("Volume aumentado para", self.volume)
            else:
                print("Volume já está no máximo")
        else:
            print("Por favor, ligue a TV primeiro")

    def decrease_volume(self):
        if self.power:
            if self.volume > 0:
                self.volume -= 1
                print("Volume diminuído para", self.volume)
            else:
                print("Volume já está no mínimo")
        else:
            print("Por favor, ligue a TV primeiro")

    def toggle_mute(self):
        if self.power:
            self.mute = not self.mute
            if self.mute:
                print("Mudo ligado")
            else:
                print("Mudo desligado")
        else:
            print("Por favor, ligue a TV primeiro")

    def git_info(self):
        print(f"TV {self.brand} / {self.size} polegadas / {self.resolution} / {self.framerate} FPS")

tv = TV("Samsung", "85", "Full HD 4K", "90")
tv.toggle_power()
tv.git_info()
tv.change_channel(5)
tv.increase_volume()
tv.decrease_volume()
tv.toggle_mute()
tv.toggle_mute()
tv.toggle_power()