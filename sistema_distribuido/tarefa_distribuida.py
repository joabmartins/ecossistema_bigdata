import paramiko

nodes = {
    'master-node': 'master',
    'worker1-node': 'worker1',
    'worker2-node': 'worker2'
}

def executar_tarefa_no_node(container_name):
    print(f"*** Conectando a {container_name}")
   # cliente = paramiko.SSHClient()
    #cliente.connect(container_name, username='root', password='admin')
    print(f"TArefa executada com sucesso em {container_name}")

def distribuir_tarefa():
    for container_name in nodes:
        executar_tarefa_no_node(container_name)

distribuir_tarefa()