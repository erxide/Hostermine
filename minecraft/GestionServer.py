import subprocess
from pathlib import Path
from .models import server
from accounts.models import CustomUser


class GestionServer:
    def __init__(self):
        self.path_script_bash = f"{Path(__file__).resolve().parent}/script/"

    def test(self):
        return self.do_command(f"{self.path_script_bash}test.sh")
    
    def create_server(self, user: CustomUser, serv : server):
        return self.do_command(f"{self.path_script_bash}create_user_dir.sh {user.username} {serv.version}")
    
    def modify_server_properties(self, user: CustomUser, serv : server):
        server_name = serv.name.replace(" ", "_")
        return self.do_command(f"{self.path_script_bash}modif_prop.sh {user} {server_name} {serv.max_players} {serv.gamemode_id.realname} {serv.difficulty_id.realname} {serv.whitelist_enabled} {serv.online_mode} {serv.pvp_enabled} {serv.command_block_enabled} {serv.allow_flight} {serv.spawn_animals} {serv.spawn_monsters} {serv.spawn_npcs} {serv.allow_nether} {serv.force_gamemode} {serv.spawn_protection}")

    def sup_server(self, user: CustomUser):
        return self.do_command(f"{self.path_script_bash}sup_server.sh {user.username}")
    
    def create_docker_compose(self, user: CustomUser, serv : server):
        return self.do_command(f"{self.path_script_bash}create_docker_compose.sh {user.username} {serv.port} {serv.version}")
    
    def run_docker(self, user : CustomUser):
        return self.do_command(f"{self.path_script_bash}run_docker.sh {user.username}")
    
    def sup_docker(self, user : CustomUser):
        return self.do_command(f"{self.path_script_bash}sup_docker.sh {user.username}")
    
    def reload_docker(self, user : CustomUser):
        return self.do_command(f"{self.path_script_bash}reload_docker.sh {user.username}")

    def do_command(self, command):
        cmd = subprocess.run(command, shell=True, capture_output=True, text=True)
        if cmd.stderr:
            return cmd.stderr
        return cmd.stdout
    
    
        

        


gestionserver = GestionServer()


if __name__ == "__main__":
    print(gestionserver.test())