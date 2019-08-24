def snake_speed(block1_mass, block2_mass, u1, u2):
    velocity = []
    if block2_mass == 0:
        velocity.append(-u1)
        return velocity
    else:
        v1 = ((block1_mass - block2_mass) / (block1_mass + block2_mass)) * u1 + (
                (2 * block2_mass) / (block1_mass + block2_mass)) * u2
        velocity.append(v1)
        v2 = ((2 * block1_mass) / (block1_mass + block2_mass)) * u1 + (
                (block2_mass - block1_mass) / (block1_mass + block2_mass)) * u2
        velocity.append(v2)
        return velocity


def list_append(list1):
    list1.append(4)
    return


def v_change(r_fll):
    return

# new = [1, 2, 3, 4]
# list_append(new)
# print(new)
