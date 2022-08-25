from kivymd.app import MDApp
from kivymd.uix.filemanager import MDFileManager
from kivymd.toast import toast

from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.dropdown import DropDown
from kivy.core.window import Window
from kivy.lang import Builder

from helpers import screen_helper
import backend

global x, y, gtype


class FileInput(Screen):
    pass


class AxisSelector(Screen):

    def setx(self):
        columns = backend.getcolumns()
        self.ids.spinner_x.values = []
        temp = []
        for i in range(len(columns)):
            temp.append(f'{i + 1} {columns[i]}')
        self.ids.spinner_x.values.extend(temp)

    def sety(self):
        columns = backend.getcolumns()
        self.ids.spinner_y.values = []
        temp = []
        for i in range(len(columns)):
            temp.append(f'{i + 1} {columns[i]}')
        self.ids.spinner_y.values.extend(temp)

    def spinnerx_clicked(self, value):
        global x
        self.ids.spinner_x.text = f'{value}'
        x = int(value.split(" ")[0])

    def spinnery_clicked(self, value):
        global y
        self.ids.spinner_y.text = f'{value}'
        y = int(value.split(" ")[0])

    pass


class GraphSelector(Screen):

    def spinner_graph_clicked(self, value):
        global gtype
        self.ids.spinner_graph.text = f'{value}'

        gtype = value

    pass


class Display(Screen):

    def img_refresh(self):
        print("in")
        self.ids.img.source = ""
        self.ids.img.source = "output.png"
    pass



sm = ScreenManager()
sm.add_widget(FileInput(name='input'))
sm.add_widget(AxisSelector(name='axis'))
sm.add_widget(GraphSelector(name='graphs'))
sm.add_widget(Display(name='disp'))


class SKETApp(MDApp):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Window.bind(on_keyboard=self.events)
        self.manager_open = False
        self.file_manager = MDFileManager(
            exit_manager=self.exit_manager,
            select_path=self.select_path,
            preview=True
        )

    def build(self):
        self.theme_cls.theme_style = 'Dark'

        screen = Builder.load_string(screen_helper)
        return screen

    def lcallback(self, dest):
        self.root.current = dest
        self.root.transition.direction = "left"

    def rcallback(self, dest):
        self.root.current = dest
        self.root.transition.direction = "right"

    def file_manager_open(self):
        self.file_manager.show('/')  # output manager to the screen
        self.manager_open = True

    def select_path(self, path):
        '''It will be called when you click on the file name
        or the catalog selection button.

        :type path: str;
        :param path: path to the selected directory or file;
        '''

        backend.readcsv(path)
        backend.clean()

        self.exit_manager()

        toast(path)
        self.root.current = "axis"

    def exit_manager(self, *args):
        '''Called when the user reaches the root of the directory tree.'''

        self.manager_open = False
        self.file_manager.close()
        # backend.getcolumns()

    def getxy(self):
        global x, y

        backend.xandy(x, y)

    def graph(self):
        global x, y, gtype
        # backend.det_graph()

        backend.plot_graph(x, y, gtype)

    def events(self, instance, keyboard, keycode, text, modifiers):
        '''Called when buttons are pressed on the mobile device.'''

        if keyboard in (1001, 27):
            if self.manager_open:
                self.file_manager.back()
        return True


SKETApp().run()
