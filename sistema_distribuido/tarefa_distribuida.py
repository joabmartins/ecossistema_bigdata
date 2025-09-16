import paramiko

nodes={
    'master-node': 'master',
    'worker-node1': 'worker1',
    'worker-node2': 'worker2'
}

def executar_tarefa_no_node(container_name):
    #simular conexão SSh para executar uma tarefa em um nó
    print(f"*** conectando a {container_name}")
    #chamar funçoes de conexão
    #cliente = paramiko.SSHClient()
    #cliente.connect(container_name, username='root', password='admin')
    print(f"Tarefa executada com sucesso em {container_name}")
def distribuir_tarefa():
    for container_name in nodes:
        executar_tarefa_no_node(container_name)
distribuir_tarefa()