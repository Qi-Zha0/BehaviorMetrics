from PyQt5.QtWidgets import (QLabel, QVBoxLayout, QWidget, QMainWindow)


class StatsWindow(QMainWindow):
    def __init__(self, parent=None, controller=None):
        super(StatsWindow, self).__init__(parent)

        self.controller = controller
        self.setWindowTitle("Metrics")
        wid = QWidget(self)
        self.setCentralWidget(wid)

        self.layout = QVBoxLayout()
        self.percentage_completed_label = QLabel("Percentage completed -> " + str(self.controller.experiment_metrics['percentage_completed']) + "%")
        self.layout.addWidget(self.percentage_completed_label)
        self.completed_distance_label = QLabel("Completed distance -> " + str(self.controller.experiment_metrics['completed_distance']) + "m")
        self.layout.addWidget(self.completed_distance_label)
        self.average_speed_label = QLabel("Average speed -> " + str(self.controller.experiment_metrics['average_speed']) + "m/s")
        self.layout.addWidget(self.average_speed_label)
        self.position_deviation_mae_label = QLabel("Position deviation MAE -> " + str(self.controller.experiment_metrics['position_deviation_mae']))
        self.layout.addWidget(self.position_deviation_mae_label)
        self.position_deviation_total_err_label = QLabel("Position deviation total error -> " + str(self.controller.experiment_metrics['position_deviation_total_err']))
        self.layout.addWidget(self.position_deviation_total_err_label)
        self.mean_brain_iterations_real_time_label = QLabel("Mean brain iterations real time -> " + str(self.controller.experiment_metrics['mean_brain_iterations_real_time']) + 's')
        self.layout.addWidget(self.mean_brain_iterations_real_time_label)
        self.brain_iterations_frequency_real_time_label = QLabel("Brain iterations frequency real time-> " + str(self.controller.experiment_metrics['brain_iterations_frequency_real_time']) + 'it/s')
        self.layout.addWidget(self.brain_iterations_frequency_real_time_label)
        self.target_brain_iterations_real_time_label = QLabel("Target brain iterations real time -> " + str(self.controller.experiment_metrics['target_brain_iterations_real_time']) + 'it/s')
        self.layout.addWidget(self.target_brain_iterations_real_time_label)

        self.brain_iterations_frequency_simulated_time_label = QLabel("Brain iterations frequency simulated time-> " + str(self.controller.experiment_metrics['brain_iterations_frequency_simulated_time']) + 'it/s')
        self.layout.addWidget(self.brain_iterations_frequency_simulated_time_label)
        self.target_brain_iterations_simulated_time_label = QLabel("Target brain iterations simulated time -> " + str(self.controller.experiment_metrics['target_brain_iterations_simulated_time']) + 'it/s')
        self.layout.addWidget(self.target_brain_iterations_simulated_time_label)

        self.mean_inference_time_label = QLabel("Mean inference time -> " + str(self.controller.experiment_metrics['mean_inference_time']) + 's')
        self.layout.addWidget(self.mean_inference_time_label)
        self.frame_rate_label = QLabel("Frame rate -> " + str(self.controller.experiment_metrics['frame_rate']) + 'fps')
        self.layout.addWidget(self.frame_rate_label)
        self.suddenness_distance = QLabel("Suddenness distance -> " + str(self.controller.experiment_metrics['suddenness_distance']))
        self.layout.addWidget(self.suddenness_distance)
        self.gpu_inference_label = QLabel("GPU inference -> " + str(self.controller.experiment_metrics['gpu_inference']))
        self.layout.addWidget(self.gpu_inference_label)
        self.mean_brain_iterations_simulated_time_label = QLabel("Mean brain iterations simulated time -> " + str(self.controller.experiment_metrics['mean_brain_iterations_simulated_time']))
        self.layout.addWidget(self.mean_brain_iterations_simulated_time_label)
        self.real_time_factor_label = QLabel("Real time factor -> " + str(self.controller.experiment_metrics['real_time_factor']))
        self.layout.addWidget(self.real_time_factor_label)
        self.real_time_update_rate_label = QLabel("Real time update rate -> " + str(self.controller.experiment_metrics['real_time_update_rate']))
        self.layout.addWidget(self.real_time_update_rate_label)
        self.experiment_total_simulated_time_label = QLabel("Experiment total simulated time -> " + str(self.controller.experiment_metrics['experiment_total_simulated_time']) + 's')
        self.layout.addWidget(self.experiment_total_simulated_time_label)
        self.experiment_total_real_time_label = QLabel("Experiment total real time -> " + str(self.controller.experiment_metrics['experiment_total_real_time']) + 's')
        self.layout.addWidget(self.experiment_total_real_time_label)

        # If lap is completed, extend information
        if 'lap_seconds' in self.controller.experiment_metrics:
            self.lap_seconds_label = QLabel(
                "Lap seconds -> " + str(self.controller.experiment_metrics['lap_seconds']) + "s")
            self.layout.addWidget(self.lap_seconds_label)
            self.circuit_diameter_label = QLabel(
                "Circuit diameter -> " + str(self.controller.experiment_metrics['circuit_diameter']) + "m")
            self.layout.addWidget(self.circuit_diameter_label)

        wid.setLayout(self.layout)


class CARLAStatsWindow(QMainWindow):
    def __init__(self, parent=None, controller=None):
        super(CARLAStatsWindow, self).__init__(parent)

        self.controller = controller
        self.setWindowTitle("Metrics")
        wid = QWidget(self)
        self.setCentralWidget(wid)

        self.layout = QVBoxLayout()
        self.completed_distance_label = QLabel("Completed distance -> " + str(self.controller.experiment_metrics['completed_distance']) + " m")
        self.layout.addWidget(self.completed_distance_label)
        self.effective_completed_distance_label = QLabel("Effective completed distance -> " + str(self.controller.experiment_metrics['effective_completed_distance']) + " m")
        self.layout.addWidget(self.effective_completed_distance_label)
        self.average_speed_label = QLabel("Average speed -> " + str(self.controller.experiment_metrics['average_speed']) + " km/h")
        self.layout.addWidget(self.average_speed_label)
        self.experiment_total_real_time_label = QLabel("Experiment total real time -> " + str(self.controller.experiment_metrics['experiment_total_real_time']) + ' s')
        self.layout.addWidget(self.experiment_total_real_time_label)
        self.experiment_total_simulated_time_label = QLabel("Experiment total simulated time -> " + str(self.controller.experiment_metrics['experiment_total_simulated_time']) + ' s')
        self.layout.addWidget(self.experiment_total_simulated_time_label)
        self.collisions_label = QLabel("Collisions -> " + str(self.controller.experiment_metrics['collisions']))
        self.layout.addWidget(self.collisions_label)
        self.lane_invasions_label = QLabel("Lane invasions -> " + str(self.controller.experiment_metrics['lane_invasions']))
        self.layout.addWidget(self.lane_invasions_label)
        self.position_deviation_mean_label = QLabel("Position deviation mean -> " + str(self.controller.experiment_metrics['position_deviation_mean']) + ' m')
        self.layout.addWidget(self.position_deviation_mean_label)
        self.position_deviation_total_err_label = QLabel("Position deviation total error -> " + str(self.controller.experiment_metrics['position_deviation_total_err']))
        self.layout.addWidget(self.position_deviation_total_err_label)
        self.mean_brain_iterations_real_time_label = QLabel("Mean brain iterations real time -> " + str(self.controller.experiment_metrics['mean_brain_iterations_real_time']) + ' s')
        self.layout.addWidget(self.mean_brain_iterations_real_time_label)
        self.brain_iterations_frequency_real_time_label = QLabel("Brain iterations frequency real time-> " + str(self.controller.experiment_metrics['brain_iterations_frequency_real_time']) + ' it/s')
        self.layout.addWidget(self.brain_iterations_frequency_real_time_label)
        self.target_brain_iterations_real_time_label = QLabel("Target brain iterations real time -> " + str(self.controller.experiment_metrics['target_brain_iterations_real_time']) + ' it/s')
        self.layout.addWidget(self.target_brain_iterations_real_time_label)
        self.mean_brain_iterations_simulated_time_label = QLabel("Mean brain iterations simulated time -> " + str(self.controller.experiment_metrics['mean_brain_iterations_simulated_time']) + ' s')
        self.layout.addWidget(self.mean_brain_iterations_simulated_time_label)
        self.brain_iterations_frequency_simulated_time_label = QLabel("Brain iterations frequency simulated time-> " + str(self.controller.experiment_metrics['brain_iterations_frequency_simulated_time']) + ' it/s')
        self.layout.addWidget(self.brain_iterations_frequency_simulated_time_label)
        self.gpu_mean_inference_time_label = QLabel("GPU mean inference time -> " + str(self.controller.experiment_metrics['gpu_mean_inference_time']) + ' s')
        self.layout.addWidget(self.gpu_mean_inference_time_label)
        self.gpu_inference_frequency_label = QLabel("GPU inference frequency -> " + str(self.controller.experiment_metrics['gpu_inference_frequency']) + ' it/s')
        self.layout.addWidget(self.gpu_inference_frequency_label)
        self.gpu_inference_label = QLabel("GPU inference -> " + str(self.controller.experiment_metrics['gpu_inference']))
        self.layout.addWidget(self.gpu_inference_label)
        self.suddenness_distance_control_commands_label = QLabel("Suddenness distance control commands -> " + str(self.controller.experiment_metrics['suddenness_distance_control_commands']))
        self.layout.addWidget(self.suddenness_distance_control_commands_label)
        self.suddenness_distance_throttle_label = QLabel("Suddenness distance throttle -> " + str(self.controller.experiment_metrics['suddenness_distance_throttle']))
        self.layout.addWidget(self.suddenness_distance_throttle_label)
        self. suddenness_distance_steer_label = QLabel("Suddenness distance steer -> " + str(self.controller.experiment_metrics['suddenness_distance_steer']))
        self.layout.addWidget(self.suddenness_distance_steer_label)
        self.suddenness_distance_brake_command_label = QLabel("Suddenness distance brake command -> " + str(self.controller.experiment_metrics['suddenness_distance_brake_command']))
        self.layout.addWidget(self.suddenness_distance_brake_command_label)
        self.suddenness_distance_control_command_per_km_label = QLabel("Suddenness distance control commandss per km -> " + str(self.controller.experiment_metrics['suddenness_distance_control_command_per_km']))
        self.layout.addWidget(self.suddenness_distance_control_command_per_km_label)
        self.suddenness_distance_throttle_per_km_label = QLabel("Suddenness distance throttle per km -> " + str(self.controller.experiment_metrics['suddenness_distance_throttle_per_km']))
        self.layout.addWidget(self.suddenness_distance_throttle_per_km_label)
        self.suddenness_distance_steer_per_km_label = QLabel("Suddenness distance steer per km -> " + str(self.controller.experiment_metrics['suddenness_distance_steer_per_km']))
        self.layout.addWidget(self.suddenness_distance_steer_per_km_label)
        self.suddenness_distance_brake_command_per_km_label = QLabel("Suddenness distance brake command per km -> " + str(self.controller.experiment_metrics['suddenness_distance_brake_command_per_km']))
        self.layout.addWidget(self.suddenness_distance_brake_command_per_km_label)
        self.suddenness_distance_speed_label = QLabel("Suddenness distance speed -> " + str(self.controller.experiment_metrics['suddenness_distance_speed']))
        self.layout.addWidget(self.suddenness_distance_speed_label)
        self.suddenness_distance_speed_per_km_label = QLabel("Suddenness distance speed per km -> " + str(self.controller.experiment_metrics['suddenness_distance_speed_per_km']))
        self.layout.addWidget(self.suddenness_distance_speed_per_km_label)
        print('LLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLL')
        print()
        print()
        print()
        print(self.controller.experiment_metrics)
        print()
        print()
        print()
        print('LLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLL')
        if 'dangerous_distance_pct_km' in self.controller.experiment_metrics:
            self.dangerous_distance_pct_km = QLabel("Percentage of dangerous distance per km -> " + str(self.controller.experiment_metrics['dangerous_distance_pct_km']))
            self.layout.addWidget(self.dangerous_distance_pct_km)
            self.close_distance_pct_km = QLabel("Percentage of close distance per km -> " + str(self.controller.experiment_metrics['close_distance_pct_km']))
            self.layout.addWidget(self.close_distance_pct_km)
            self.medium_distance_pct_km = QLabel("Percentage of medium distance per km -> " + str(self.controller.experiment_metrics['medium_distance_pct_km']))
            self.layout.addWidget(self.medium_distance_pct_km)
            self.great_distance_pct_km = QLabel("Percentage of great distance per km -> " + str(self.controller.experiment_metrics['great_distance_pct_km']))
            self.layout.addWidget(self.great_distance_pct_km)

        wid.setLayout(self.layout)