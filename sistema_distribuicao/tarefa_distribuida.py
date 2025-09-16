# pip install paramiko
import paramiko

nodes = { 
    'master-node': 'master',
    'worker1-node': 'worker1',
    'worker2-node': 'worker2'
    }


def executar_tarefa_no_node(container_name):
# simular uma conexao SSH para executar uma tarefa em um nó
    print(f"*** Conectando a {container_name}")
    # chamar as funções de conexão
   # cliente = paramiko.SSHCLient()
    # cliente.connect(container_name, username= 'root', passwork='admin')
    # confirmar execução
    print(f"Tarefa executada co sucesoo em {container_name}")


def distribuir_tarefa():
    # distribuir uma tarefa simples para todos os nós do cluster
    for container_name in nodes:
        executar_tarefa_no_node(container_name)

distribuir_tarefa()        

    
