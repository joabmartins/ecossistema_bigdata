import paramiko

nodes = {
    'master-node': 'master',
    'worker1-node': 'worker1',
    'worker2-node': 'worker2'
}

def executar_tarefa_no_node( container_name ):
    # simular um conexão SSH para executar uma tarefa em um nó.
    print(f" *** Conectando a { container_name }")
    # Chamar ad funções de conexão.
    # cliente = paramiko.SSHClient( )
    # cliente.connect( container_name, username='root', password='admin' )
    # Confirmar execução
    print(f"tarefa executada com sucesso em { container_name }")

def distribuir_tarefa( ):
    # Distribuir uma tarefa simples para todos os nós do cluster.
    for container_name in nodes:
        executar_tarefa_no_node( container_name )    

distribuir_tarefa( )