from multiping import MultiPing


if __name__ == "__main__":

    # Lista de endereço dos AP's
    addrs = ["192.168.3.209", "192.168.3.210", "192.168.3.211"]

    print("Enviando Primeira Rodada de Ping's")
    mp = MultiPing(addrs)
    mp.send()
    #Primeira tentativa de Ping, espera-se que a conexão esteja perfeita se a resposta for recebida aqui
    responses, no_responses = mp.receive(0.01)

    print("   AP's online:  %s" % list(responses.keys()))
    print("   AP's sem resposta: %s" % no_responses)

    #Segunda tentativa de Ping, espera-se que a conexão esteja estavel porém com latência acima de 1ms
    print("   --- Verificando novos retornos ---")
    responses, no_responses = mp.receive(0.1)
    print("   AP's online:  %s" % list(responses.keys()))
    print("   AP's ainda sem resposta:  %s" % no_responses)
    print("")

    #Terceira tentativa de Ping com novos parâmetros, aguardando latência de até 10ms
    #Caso não haja resposta aqui, o AP está offline.
    print("Ultima verificação")
    mp = MultiPing(addrs)
    for i in range(3):
        mp.send()
        responses, no_response = mp.receive(0.01)

        print("    AP's online:     %s" % list(responses.keys()))
        if not no_response:
            print("    Todos AP's online")
            break
        else:
            print("    %d. Tentando novamente para: %s" % (i + 1, no_response))
    if no_response:
        print("    AP's offline: %s" %
              no_response)
    print("")