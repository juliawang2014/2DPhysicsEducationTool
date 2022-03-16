def display_values(object, type="velocity"):
    """Returns one of the following values as determined by the type parameter:

    velocity, angular_velocity, mass, moment, force, angle, position, center_of_gravity, torque"""
    
    if type == "velocity":
        return object.velocity
    elif type == "angular_velocity":
        return object.angular_velocity
    elif type == "mass":
        return object.mass
    elif type == "moment":
        return object.moment
    elif type == "force":
        return object.force
    elif type == "angle":
        return object.angle
    elif type == "position":
        return object.angle
    elif type == "center_of_gravity":
        return object.center_of_gravity
    elif type == "torque":
        return object.torque