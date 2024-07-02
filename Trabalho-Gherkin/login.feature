Feature: Login de Usuário

Descrição: 
    Esta feature garante que os usuários possam se autenticar no sistema e acessar suas contas.

Cenário: Login com Sucesso
    Dado que um usuário cadastrado esteja tentando fazer login
    Quando ele insere suas credenciais válidas
    Então o sistema deve permitir o login e conceder acesso à sua conta

Cenário: Login com Credenciais Inválidas
    Dado que um usuário esteja tentando fazer login
    Quando ele insere credenciais inválidas
    Então o sistema deve exibir uma mensagem de erro informando que as credenciais estão incorretas
