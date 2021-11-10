import player_control as pc
import mesh_functions as mf
from sys import exit

new_mesh = mf.create_new_mesh()
mf.render(new_mesh)

while True:

    user = input('enter w for up, s for down, a for left, and d for right movement, and q for quiting\n')

    if user.lower() == 'w':
        pc.up(new_mesh)
        mf.refresh(new_mesh)

    elif user.lower() == 's':
        pc.down(new_mesh)
        mf.refresh(new_mesh)

    elif user.lower() == 'a':
        pc.left(new_mesh)
        mf.refresh(new_mesh)

    elif user.lower() == 'd':
        pc.right(new_mesh)
        mf.refresh(new_mesh)

    elif user.lower() == 'q':
        exit(0)

    else:
        print('did not compute')