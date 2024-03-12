from django.db import models

class Usuario(models.Model):
    nome = models.CharField(max_length=100)
    cpf = models.IntegerField(max_length=100)
    email = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = 'Usuarios'

    def __str__(self):
        return f'{self.nome}'
    
class Genero(models.Model):
    nome = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = 'Generos'

    def __str__(self):
        return self.nome

class Cidade(models.Model):
    nome = models.CharField(max_length=100)
    estado = models.CharField(max_length=2)

    class Meta:
        verbose_name_plural = 'Editoras'

    def __str__(self):
        return f'{self.nome}'
    
class Editora(models.Model):
    nome = models.CharField(max_length=100)
    site = models.CharField(max_length=100)
    cidade = models.ForeignKey(Cidade, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'Editoras'


    def __str__(self):
        return f'{self.nome}'
        
class Autor(models.Model):
    nome = models.CharField(max_length=100)
    cidade = models.ForeignKey(Cidade, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'Autores'


    def __str__(self):
        return f'{self.nome}'

class Livro(models.Model):
    nome = models.CharField(max_length=100)
    genero = models.ForeignKey(Genero, on_delete=models.CASCADE)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
    editora = models.ForeignKey(Editora, on_delete=models.CASCADE)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    datapublicacao = models.DateField()
    imagem = models.ImageField(upload_to='static/', blank=True)
    class Meta:
        verbose_name_plural = 'Livros'

    def __str__(self):
        return f'{self.nome}'
        
class Emprestimo(models.Model):
    dataemprestimo = models.DateField()
    livro = models.ForeignKey(Livro, on_delete=models.CASCADE)
    datadevolucao = models.DateField()
    leitor = models.ForeignKey(Usuario, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'Emprestimos'

    def __str__(self):
        return f'{self.livro} '