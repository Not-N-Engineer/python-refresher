import numpy as np
import matplotlib.pyplot as plt


class AUVPhysics:
    '''Calculates bouyancy
       V: volume displaced by object in m^3
       density: density of outside fluid in kg/m^3'''
    def calculate_bouyancy(V, density):
        g = 9.81
        Fb = g * V * density
        return Fb

    '''Calculates whether gravity is less than the bouyant force of an object submerged in water
       V: volume displaced by object in m^3
       m: mass of object in kg'''
    def will_it_float(V, m):
        g = 9.81
        Fg = g * m
        Fb = AUVPhysics.calculate_bouyancy(V, 1000)
        return Fg < Fb

    '''Calculates pressure experienced in a given depth of water
       depth: depth in m'''
    def calculate_pressure(depth):
        g = 9.81
        density = 1000
        pressure = g * depth * density
        return pressure

    '''Calculates simple acceleration
       F: force exerted on the object in m*kg/s^2
       m: mass of object in kg'''
    def calculate_acceleration(F, m):
        if m == 0:
            raise ValueError
        acceleration = F / m
        return acceleration

    '''Calculates angular acceleration
       torque: torque in kg*m^2/s^2
       I: the moment of inertia of the object in kg*m^2'''
    def calculate_angular_acceleration(torque, I):
        if I == 0:
            raise ValueError
        angular_acceleration = torque / I
        return angular_acceleration

    '''Calculates torque experienced by an object
       F_magnitude: the magnitude of the force acting on the object in m*kg/s^2
       F_direction: the direction in which the force is acting in relation to the center of mass in RADIANS
       r: the radius from the center of mass where the force is acting in m'''
    def calculate_torque(F_magnitude, F_direction, r):
        F_rotation = F_magnitude/np.cos(F_direction)
        torque = r * F_rotation
        return torque

    '''Calculates inertia
       m: mass of the object in kg
       r: distance from the axis of rotation of the object in m'''
    def calculate_moment_of_inertia(m, r):
        if not isinstance(m, (int, float)):
            raise TypeError
        inertia = m * (r**2)
        return inertia



class AUV1:
    '''Calculates the acceleration in the x direction of a simple AUV
       F_magnitude: the force applied by the thruster in m*kg/s^2
       F_angle: the angle the thruster is at in RADIANS
       m: the mass of the AUV in kg
       V: the volume of the AUV in m^3
       thruster_distance: the distance betweent he thruster and the center of mass in m'''
    def calculate_auv_acceleration(F_magnitude, F_angle, m):
        # Get the force in the x direction
        F_x = F_magnitude/np.cos(F_angle)

        return AUVPhysics.calculate_acceleration(F_x, m)

    '''Calculates the angular acceleration of a simple AUV
       F_magnitude: the force applied by the thruster in m*kg/s^2
       F_angle: the angle the thruster is at in RADIANS
       I: the moment of inertia of the AUV in kg*m^2
       thruster_distance: the distance betweent he thruster and the center of mass in m'''
    def calculate_auv_angular_acceleration(F_magnitude, F_angle, I = 1, thruster_distance = 0.5):
        torque = AUVPhysics.calculate_torque(F_magnitude, F_angle + 90, thruster_distance)
        return AUVPhysics.calculate_angular_acceleration(torque, I)



class AUV2:
    '''Calculates the angular acceleration of an AUV and returns the acceleration vector
       T: an array the forces applied by each thruster in m*kg/s^2
       thruster_angle: the angle the thruster is at in RADIANS
       auv_angle: the angle the AUV is at in radians
       m: mass of the AUV in kg'''
    def calculate_auv2_acceleration(T: np.ndarray, thruster_angle, auv_angle, m = 100):
        # THETA direction
        # Get the forces in the theta direction if applicable
        if(not (thruster_angle in (np.pi/2, 3*np.pi/2, 5*np.pi/2, -np.pi/2, -3*np.pi/2, -5*np.pi/2))):
            f1 = T[0]*np.cos(thruster_angle)
            f2 = T[1]*np.cos(thruster_angle)
            f3 = -T[2]*np.cos(thruster_angle)
            f4 = -T[3]*np.cos(thruster_angle)

            # Accelerations
            a1 = AUVPhysics.calculate_acceleration(f1, m)
            a2 = AUVPhysics.calculate_acceleration(f2, m)
            a3 = AUVPhysics.calculate_acceleration(f3, m)
            a4 = AUVPhysics.calculate_acceleration(f4, m)

            total_acceleration_theta = a1 + a2 + a3 + a4

            acceleration_x = total_acceleration_theta*np.cos(auv_angle)
            acceleration_y = total_acceleration_theta*np.sin(auv_angle)
        else:
            acceleration_x = 0
            acceleration_y = 0

        #PERPENDICULAR direction
        # Get the forces in the perpendicular direction if applicable
        if(not (thruster_angle in (0, np.pi, 2*np.pi, -np.pi, -2*np.pi))):
            f1 = T[0]*np.sin(thruster_angle)
            f2 = -T[1]*np.sin(thruster_angle)
            f3 = -T[2]*np.sin(thruster_angle)
            f4 = T[3]*np.sin(thruster_angle)
        
            # Accelerations
            a1 = AUVPhysics.calculate_acceleration(f1, m)
            a2 = AUVPhysics.calculate_acceleration(f2, m)
            a3 = AUVPhysics.calculate_acceleration(f3, m)
            a4 = AUVPhysics.calculate_acceleration(f4, m)

            total_acceleration_perpendicular = a1 + a2 + a3 + a4

            acceleration_x += total_acceleration_perpendicular*np.cos(auv_angle)
            acceleration_y += total_acceleration_perpendicular*np.sin(auv_angle)
        
        return np.array([acceleration_x, acceleration_y])


    '''Calculates the angular acceleration of an AUV and returns the acceleration vector
       T: an array the forces applied by each thruster in m*kg/s^2
       thruster_angle: the angle the thruster is at in RADIANS
       distance_L: distance of thruster from center along the length
       distance_l: distance of thruster from center along the width
       I: the moment of inertia of the AUV in kg*m^2'''
    def calculate_auv2_angular_acceleration(T: np.ndarray, thruster_angle, distance_L, distance_l, I = 100):
        distance = np.sqrt(distance_L**2 + distance_l**2)                      # Calculate the distance
        angle_ctAxis_yAxis = np.arctan2(distance_L, distance_l)                # Calculate the angle between the local y-axis and the axis running through the center and thruster
        angle_ctPerpendicular_alpha = 90 - thruster_angle - angle_ctAxis_yAxis # Finally, calculate the angle between the thruster and the perpendicular from the thruster of the axis running through the center and thruster

        # Torques
        τ1 = AUVPhysics.calculate_torque(T[0], angle_ctPerpendicular_alpha, distance)
        τ2 = -AUVPhysics.calculate_torque(T[1], angle_ctPerpendicular_alpha, distance)
        τ3 = AUVPhysics.calculate_torque(T[2], angle_ctPerpendicular_alpha, distance)
        τ4 = -AUVPhysics.calculate_torque(T[3], angle_ctPerpendicular_alpha, distance)

        # Angular Accelerations
        a_a1 = AUVPhysics.calculate_angular_acceleration(τ1, I)
        a_a2 = AUVPhysics.calculate_angular_acceleration(τ2, I)
        a_a3 = AUVPhysics.calculate_angular_acceleration(τ3, I)
        a_a4 = AUVPhysics.calculate_angular_acceleration(τ4, I)

        return a_a1 + a_a2 + a_a3 + a_a4
    

    def simulate_auv2_step(T: np.ndarray, thruster_angle, distance_L, distance_l, m, I, x, y, theta, vx, vy, a_v, dt):
        # 1. Find New Acceleration vector and angular acceleration
        a = AUV2.calculate_auv2_acceleration(T, thruster_angle, theta, m)*dt
        a_a = AUV2.calculate_auv2_acceleration(T, thruster_angle, distance_L, distance_l, I)*dt

        # 2. Find the new velocities and angular velocity
        vx += a[0]
        vy += a[1]
        a_v += a_a

        # 3. Find the new positions and angle
        x += vx
        y += vy
        theta += a_v

        return [x, y, theta, vx, vy, a_v, a]


    def simulate_auv2_motion(T: np.ndarray, thruster_angle, distance_L, distance_l, m = 100, I = 100, dt = 0.1, t_final = 10, x0 = 0, y0 = 0, theta0 = 0):
        t = np.ndarray([0])
        x = np.ndarray([x0])
        y = np.ndarray([y0])
        theta = np.ndarray([theta0])
        v = np.ndarray([[0, 0]])
        a_v = np.ndarray([0])
        a = np.ndarray([[0,0]])

        for i in range(0, t_final, dt):
            step = AUV2.simulate_auv2_step(T, thruster_angle, distance_L, distance_l, m, I, x[i], y[i], theta[i], v[i][0], v[i][1], a_v[i], dt)
            t = np.append(t[i]+dt)
            x = np.append(step[0])
            y = np.append(step[1])
            theta = np.append(step[2])
            v = np.append([step[3], step[4]])
            a_v = np.append(step[5])
            a = np.append(step[6])
        
        return [t, x, y, theta, v, a_v, a]
    

    def plot_auv2_motion(t, x, y, theta, v, a_v, a): # all np.ndarrays     
        plt.plot(t, [x, y], label="Position")
        plt.plot(t, v, label="Velocity")
        plt.plot(t, a, label="Acceleration")
        plt.xlabel("Time (s)")
        plt.ylabel("Position (m), Velocity (m/s), Acceleration (m/s^2)")
        plt.legend()
        plt.show()


