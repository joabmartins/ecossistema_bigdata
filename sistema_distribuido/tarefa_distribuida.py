import paramiko

nodes = {
     'master-node': 'master',
     'worker1-node': 'worker1',
     'worker2-node': 'worker2'
}

def executar_tarefa_no_node(container_name):
    # Simular um conexão SSH para executar uma tarefa me um nó
    print(f" *** Conectando a {container_name}")
    # Chamar funções de conexão
    # cliente = paramiko.SSHCliente()
    # cliente.connect(container_name, username='root', password='admin')
    # Confirmar execução
    print(f"Tarefa executada com sucesso em {container_name}")

    
def distribuir_tarefa():
    #Distibuir uma tarefa simples para todos os nós do cluster
    for container_name in nodes:
        executar_tarefa_no_node(container_name)

distribuir_tarefa()