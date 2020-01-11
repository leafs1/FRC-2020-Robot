/*----------------------------------------------------------------------------*/
/* Copyright (c) 2018-2019 FIRST. All Rights Reserved.                        */
/* Open Source Software - may be modified and shared by FRC teams. The code   */
/* must be accompanied by the FIRST BSD license file in the root directory of */
/* the project.                                                               */
/*----------------------------------------------------------------------------*/

package frc.robot;

import java.util.ArrayList;

/**
 * The Constants class provides a convenient place for teams to hold robot-wide numerical or boolean
 * constants.  This class should not be used for any other purpose.  All constants should be
 * declared globally (i.e. public static).  Do not put anything functional in this class.
 *
 * <p>It is advised to statically import this class (or one of its inner classes) wherever the
 * constants are needed, to reduce verbosity.
 */
public final class Constants {
    public static final class ClimberConstants {
        public static final int kElevatorXMotorPort = 5;
        public static final int kElevatorYMotorPort = 6;
    }
    public static final class ShooterConstants {
        public static final int kShooterMotorPort = 7;
    }
    public static final class MotorConstants{
        public static final int kLeftMotorPort = 0;
        public static final int kRightMotorPort = 2;
    }

    public static final class EncoderConstants{
        public static final int kRightEncoderA = 0;
        public static final int kRightEncoderB = 6;
        public static final int kLeftEncoderA = 2;
        public static final int kLeftEncoderB = 7;
        public static final int kElevatorEncoderA = 4;
        public static final int kElevatorEncoderB = 5;
        //placeholder value
        public static final double ENCODER_COUNTS_PER_INCH = 13.49;
    }

    public static final class CameraConstants{
        // placeholder values since we don't know what servo they will be plugged into yet
        public static final int kCameraXServoRange = 1;
        public static final int kCameraYServoRange = 3;

    }

    
  


}
