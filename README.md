<h1> M5 - Kiosque </h1>

<h2> Como rodar os testes localmente </h2>

<h3> Preparação do ambiente <h3>

<p>Instalar o pacote <strong>pytest-testdox</strong>:</p>

```shell
pip install pytest-testdox
```

<p>Rodar os testes referentes a cada tarefa isoladamente:</p>

```shell
pytest --testdox -vvs caminho/para/o/modulo/da/tarefa
```

Exemplo:
<ul>
<li>Tarefa 1</li>

```shell
pytest --testdox -vvs tests/tarefas/tarefa_1/
```

<li>Tarefa 2</li>

```shell
pytest --testdox -vvs tests/tarefas/tarefa_2/
```
<li>Tarefa 3</li>

```shell
pytest --testdox -vvs tests/tarefas/tarefa_3/
```

</ul>

### **Importante!!**
Caso esteja utilizando Windows e, ao rodar o comando `pytest --testdox` aparecer um erro de **cmdlet**, troque o inicio do comando pelo seguinte:

```shell
python -m pytest --testdox
```

<hr>
<p>Você também pode rodar cada método de teste isoladamente:</p>

```shell
pytest --testdox -vvs caminho/para/o/arquivo/de/teste::NomeDaClasse::nome_do_metodo_de_teste
```

<p>Exemplo: executar somente "test_can_get_product_by_id".</p>

```shell
pytest --testdox -vvs tests/tarefas/tarefa_1/test_get_product_by_id.py::TestGetProductById::test_can_get_product_by_id
```
<hr>
<p>Os testes referentes as funcionalidades extras não são executados por padrão caso você não especifique o caminho até eles. Então caso você queira os executar, rode:</p>

```shell
pytest --testdox -vvs tests/tarefas/tarefa_3/extra_add_product.py
```

## Rodando todos os testes

Para rodar todos os testes da aplicação de uma vez, execute o seguinte comando no terminal (estando na raiz do projeto)

```shell
pytest --testdox
```
