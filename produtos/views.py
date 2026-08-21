from django.shortcuts import render

def retunProdutos():
    produtos = [
        {'id': 1, 
         'nome': 'Fone sem fio',
         'lote': '001',
         'categoria': 'Eletrônicos',
         'quantidade': 3
         },
        {'id': 2, 
         'nome': 'Vestido mid',
         'lote': '002',
         'categoria': 'Vestiário',
         'quantidade': 6
         },
        {'id': 3, 
         'nome': 'Base Dior',
         'lote': '003',
         'categoria': 'Cosméticos',
         'quantidade': 2
         },
        {'id': 4, 
         'nome': 'Máquina de lavar roupa',
         'lote': '004',
         'categoria': 'Eletrodoméstico',
         'quantidade': 8
         },
        {'id': 5, 
         'nome': 'Cif multiuso',
         'lote': '005',
         'categoria': 'Limpeza',
         'quantidade': 19
         }
    ]
    return produtos

# Create your views here.
def listagem(request):
    context = {'produtos': retunProdutos()}
    return render(request, 'produtos/listagem.html', context)

def detalhes(request, id):
    for item in retunProdutos():
        if item['id'] == id:
            context = item
    return render(request, 'produtos/detalhes.html', context)