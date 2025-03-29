class Smartphone:
    """Represents a smartphone with its attributes and functionalities."""

    def __init__(self, brand, model, storage, camera_resolution, battery_capacity):
        """Initializes a Smartphone object."""
        self.brand = brand
        self.model = model
        self.storage = storage
        self.camera_resolution = camera_resolution
        self.battery_capacity = battery_capacity
        self.is_on = False
        self.apps = []

    def power_on(self):
        """Turns the smartphone on."""
        self.is_on = True
        print(f"{self.brand} {self.model} is powering on.")

    def power_off(self):
        """Turns the smartphone off."""
        self.is_on = False
        print(f"{self.brand} {self.model} is powering off.")

    def install_app(self, app_name):
        """Installs a new app."""
        if self.is_on:
            self.apps.append(app_name)
            print(f"{app_name} installed successfully.")
        else:
            print("Please turn on the phone first.")

    def uninstall_app(self, app_name):
        """Uninstalls an app."""
        if self.is_on and app_name in self.apps:
            self.apps.remove(app_name)
            print(f"{app_name} uninstalled successfully.")
        elif not self.is_on:
            print("Please turn on the phone first.")
        else:
            print(f"{app_name} is not installed.")

    def display_info(self):
        """Displays the smartphone's information."""
        print(f"Brand: {self.brand}")
        print(f"Model: {self.model}")
        print(f"Storage: {self.storage} GB")
        print(f"Camera Resolution: {self.camera_resolution} MP")
        print(f"Battery Capacity: {self.battery_capacity} mAh")
        print(f"Apps installed: {', '.join(self.apps)}")
        print(f"Power status: {'On' if self.is_on else 'Off'}")

#Inheritance example. A gaming smartphone.

class GamingSmartphone(Smartphone):
    """Represents a gaming-focused smartphone, inheriting from Smartphone."""

    def __init__(self, brand, model, storage, camera_resolution, battery_capacity, cooling_system, refresh_rate):
        """Initializes a GamingSmartphone object, adding gaming-specific attributes."""
        super().__init__(brand, model, storage, camera_resolution, battery_capacity)
        self.cooling_system = cooling_system
        self.refresh_rate = refresh_rate

    def display_info(self):
        """Overrides the display_info method to include gaming features."""
        super().display_info()
        print(f"Cooling System: {self.cooling_system}")
        print(f"Refresh Rate: {self.refresh_rate} Hz")

