from pandaeditor import *

class Draggable(Button):

    def __init__(self, **kwargs):
        super().__init__()
        self.drag_target = self
        self.require_key = None
        self.dragging = False
        self.start_pos = self.position

        self.x_lock = False
        self.y_lock = False

        for key, value in kwargs.items():
            setattr(self, key, value)


    def input(self, key):
        super().input(key)
        # if key == 'tab':
        #     Draggable.drag_mode = not Draggable.drag_mode
        #     Draggable.label.enabled = not Draggable.label.enabled

        if self.hovered and key == 'left mouse down':
            if not self.require_key or held_keys[self.require_key]:
                self.dragging = True
                self.start_pos = self.position
                try:
                    self.drag()
                except:
                    pass

        if key == 'left mouse up':
            self.dragging = False
            self.delta_drag = self.position - self.start_pos
            try:
                self.drop()
            except:
                print('no drop func')
                pass


    def update(self, dt):
        if self.dragging:
            if not self.x_lock:
                self.drag_target.world_x += mouse.velocity[0] * camera.fov
            if not self.y_lock:
                self.drag_target.world_y += mouse.velocity[1] * camera.fov



if __name__ == '__main__':
    app = PandaEditor()
    camera.orthographic = True

    e = Draggable()
    e.parent = scene
    # e.require_key = 'shift'
    app.run()
