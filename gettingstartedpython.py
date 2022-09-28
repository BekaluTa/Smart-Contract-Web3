from algosdk import account,mnemonic
def generate_algorand_keypair():
    private_key,address=account.generate_account()
    print("my Addresse:{}".format(address))
    print("My Private Key:{}".format(private_key))
    print("my Passphrase:{}".format(mnemonic.from_private_key(private_key)))
    
generate_algorand_keypair()

#my Addresse:XLZMD3XWXLIESLFYMVX2KXY7PSW3FC2BQELJLETZQPJ5GKL4ZU3IJZNLYY
#My Private Key:GhZeY44SNhUGBFUgN5QnJRnZ7AJFgHJgbBcciW7ZbHS68sHu9rrQSSy4ZW+lXx98rbKLQYEWlZJ5g9PTKXzNNg==
#my Passphrase:select joke coyote cigar history luxury cage fence tomato express need myself rate robot chimney leopard atom ranch arm mushroom tackle curve pet about asthma