# Para instalar um comando = pip install + comando
import paramiko

nodes = {
    'master-node': 'master',
    'worker1-node': 'worker1',
    'worker2-node': 'worker2'
}

def executar_tarefa_no_node(container_name):
    # Simular uma conexão SSH para executar uma tarefa em um nó
    print(f" *** conectando a {container_name}")
    # Chamar as funções de conexão
    #cliente = paramiko.SSHClient()
    #cliente.connect(container_name, username='root', password='admin')
    # Confirmar execução
    print(f"Tarefa executada com sucesso em {container_name}")

def distribuir_tarefa():
    # Distruibuir uma tarefa simples para todos os nós do cluster
    for container_name in nodes:
        executar_tarefa_no_node(container_name)

distribuir_tarefa()