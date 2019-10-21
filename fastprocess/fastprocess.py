import os
import signal

class FastProcess:
    def __init__(self, cmd, stdin=None, stdout=None, stderr=None, env=None):
        file_actions = []
        if stdin:
            file_actions.append((os.POSIX_SPAWN_DUP2, stdin.fileno(), 0))
        if stdout:
            file_actions.append((os.POSIX_SPAWN_DUP2, stdout.fileno(), 1))
        if stderr:
            file_actions.append((os.POSIX_SPAWN_DUP2, stderr.fileno(), 2))
        self.pid = os.posix_spawnp(cmd[0], cmd, env if env else os.environ, file_actions=file_actions)

    def __del__(self):
        os.kill(self.pid, signal.SIGTERM)

    def terminate(self):
        os.kill(self.pid, signal.SIGTERM)

    def signal(self, sig):
        os.kill(self.pid, sig)

    def wait(self):
        return os.WEXITSTATUS(os.waitpid(self.pid, 0)[1])


class OldFastProcess:
    def __init__(self, cmd, stdin=None, stdout=None, stderr=None):
        self.pid = os.fork()
        if self.pid == 0:
            if stdin:
                os.dup2(stdin.fileno(), 0)
            if stdout:
                os.dup2(stdout.fileno(), 1)
            if stderr:
                os.dup2(stderr.fileno(), 2)
            os.execvp(cmd[0], cmd)

    def __del__(self):
        os.kill(self.pid, signal.SIGTERM)

    def terminate(self):
        os.kill(self.pid, signal.SIGTERM)

    def signal(self, sig):
        os.kill(self.pid, sig)

    def wait(self):
        return os.WEXITSTATUS(os.waitpid(self.pid, 0)[1])
