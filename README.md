# PL-Projeto

## 2.6 Conversor toml-json

Ver detalhes em: <https://github.com/toml-lang/toml>
A linguagem toml permite uma fácil definição de estruturas complexas (dicionários generalizados) frequentmente usados em
ficheiros de configuração e em vários outros domínios de modo análogo ao JSON e ao YAML
Considere o sequinte exemplo:

    title = "TOML Example"

    [owner]
        name = "Tom Preston-Werner"
        date = 2010-04-23
        time = 21:30:00
    
    [database]
        server = "192.168.1.1"
        ports = [ 8001, 8001, 8002 ]
        connection_max = 5000
        enabled = true
    
    [servers]
        [servers.alpha]
        ip = "10.0.0.1"
        dc = "eqdc10"

        [servers.beta]
        ip = "10.0.0.2"
        dc = "eqdc10"
    
    #Line breaks are OK when inside arrays
    
    hosts = [
    "alpha",
    "omega"
    ]

Pretende-se construir uma ferramenta (Flex,Yacc) que converta um subconjunto de Toml para JSON.
