import dearpygui.dearpygui as dpg


class MainWindow:
    def __init__(self, width, height):
        self.__width = width
        self.__height = height
        self.__title = "Spotube"
        self.setup()

    def save_callback(self):
        input_text = dpg.get_value("string")
        print(f"Save Clicked {input_text}")

    def save_callback_two(self):
        input_text = dpg.get_value("string2")
        print(f"Save Clicked {input_text}")

    def setup(self):
        dpg.create_context()

        with dpg.window(tag="Primary Window"):
            dpg.add_text(default_value="Spotify Client", label="Spotify Client")
            dpg.add_input_text(label="Path", hint="Quick brown fox", tag="string")
            dpg.add_button(label="Save", callback=self.save_callback)
            dpg.add_text(default_value="Youtube Client", label="Youtube Client")
            dpg.add_input_text(label="Path", hint="Quick brown fox")
            dpg.add_button(label="Save", callback=self.save_callback_two)
            dpg.add_text(default_value="Output", label="Output")
            dpg.add_input_text(label="Path", hint="Quick brown fox")

        dpg.create_viewport(title='Spotube', width=self.__width, height=self.__height)
        dpg.setup_dearpygui()
        dpg.show_viewport()
        dpg.set_primary_window("Primary Window", True)
        dpg.start_dearpygui()
        dpg.destroy_context()
