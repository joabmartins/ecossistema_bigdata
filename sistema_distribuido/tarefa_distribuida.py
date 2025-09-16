# pip install paramiko
import paramiko

nodes = {
    'master-node': 'master', 
    'worker1-node': 'worker1',
    'worker2-node': 'worker2'
}

def  executar_tarefa_no_node(container_name):
    # simular uma conexão SSH para executar uma tarefa em um nó
    print(f" *** Conectando a {container_name}")
    # chamar as funções de conexão
    #cliente = paramiko.SSHCLIENT()
    #cliente.connect(container_name, username='root', password='admin')
    # confirmar conexão
    print(f"Tarefa executada com sucesso em {container_name}")


def distribuir_tarefa():
    # Distribuir uma tarefa simples para todos os nós do cluster
    for container_name in nodes:
        executar_tarefa_no_node(container_name)

distribuir_tarefa()
