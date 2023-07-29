def draw_ruler(inches, tick_length):
    """Draw Line"""
    draw_line(tick_length, '0')
    for j in range(1, 1 + inches):
        draw_interval(tick_length - 1)
        draw_line(tick_length, str(j))


def draw_line(tick_length, tick_label=""):
    line = "-" * tick_length
    if tick_label:
        line += ' ' + tick_label
    print(line)

def draw_interval(center_length):
    if center_length > 0:
        draw_interval(center_length - 1)
        draw_line(center_length)
        draw_interval(center_length - 1)


total_rular_size = int(input("Please write a number to draw total inches of Ruler: "))
tick_size = int(input("Please write a number for tick size: "))

draw_ruler(total_rular_size, tick_size)