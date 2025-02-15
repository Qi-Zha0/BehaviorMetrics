from brains.gazebo.f1.rl_utils.env_type import EnvironmentType
from brains.gazebo.f1.rl_utils.exceptions import NoValidEnvironmentType
from brains.gazebo.f1.rl_utils.models.f1_env_camera import QlearnF1FollowLineEnvGazebo
from brains.gazebo.f1.rl_utils.models.followline_dqn_tf import FollowLineDQNF1GazeboTF


class F1Env:

    def __new__(cls, **config):
        task = config.get("task")

        # Qlearn F1 FollowLine camera
        if task == EnvironmentType.qlearn_env_camera_follow_line.value:
            return QlearnF1FollowLineEnvGazebo(**config)
        elif task == EnvironmentType.dqn_env_follow_line.value:
            return FollowLineDQNF1GazeboTF(**config)
        else:
            raise NoValidEnvironmentType(task)
