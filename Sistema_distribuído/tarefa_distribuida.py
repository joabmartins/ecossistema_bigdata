import paramiko

nodes = { 
    'master-node': 'master',
    'workerl-node': 'worker1'
    'worker2-node' 'worker2'
}

def executar_tarefa_no_node(container_name):
    # Simular uma conexâo SSH para executar uma tarea em um nó
    print(f" *** Conectando a {container_name}")
    # Chamar funçôes de conexâo
    # cliente = paramiko.SSHClient()
    # cliente.connect(container_name, username='root', password='admin')

    print(f"tarefa executada com sucesso em {container_name}")

def distribuir_tarefa():
    # Distribuir uma tarefa simples para todos nós do cluster
    for container_name in nodes:
        executar_tarefa_no_node(container_name)

distribuir_tarefa()