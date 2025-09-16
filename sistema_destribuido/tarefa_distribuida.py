#pip intall paramiko
import paramiko

nodes = {
    'master-node': 'master',
    'worker1-node': 'worker1',
    'worker2-node': 'worker2'
}

def executar_tarefa_no_node(container_name):
    #simular uma conexão ssh para execuar uma tarefa em um nó
    print(f" *** conectando a {container_name}")
    #chamar as funções de conexão
    #cliente = paramiko.SHHClient()
    #cliente.connect(container_name, username='root', password='admin')
    #confirmar execução
    print(f"tarefa executada com sucesso em {container_name}")

def distribuir_tarefa():
    #dsitribuir uma tarefa simples para todos os nós do cluster
    for container_name in nodes:
        executar_tarefa_no_node(container_name)
    
distribuir_tarefa()