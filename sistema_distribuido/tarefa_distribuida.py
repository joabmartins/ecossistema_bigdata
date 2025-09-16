import paramiko

nodes = {
    'master-node': 'master',
    'worker1-node': 'worker1',
    'worker2-node': 'worker2'
}

def executar_tarefa_no_node(container_name):
    # Simular uma conexão SSH para executar uma tarefa em um nó
    print(f" *** conectando a {container_name}") 
    # Chamar as funcões de conexão
    #cliente = paramiko.SSHClient()
    #cliente.conectar(container_name, username='root', password='admin')
    # Confrmar execução
    print(f"Tarefa executada com sucesso em {container_name}")

def distrbuir_tarefa():
    # Distribuir uma tarefa simples para todos os n´s do cluster
    for container_name in nodes:
        executar_tarefa_no_node(container_name)

distrbuir_tarefa()