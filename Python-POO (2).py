#!/usr/bin/env python
# coding: utf-8

# # Programacion Orientada a Objetos
# ![image.png](attachment:image.png)
# 
# Este notebook incluye una introduccion a la Programación Orientada a Objetos POO o OOP en inglés. Se trata de un paradigma de programación introducido en los años 1970s, pero que no se hizo popular hasta años más tarde. <br>
# 
# Este modo o paradigma de programación nos permite organizar el código de una manera que se asemeja bastante a como pensamos en la vida real, utilizando las famosas **clases**. Estas nos permiten agrupar un conjunto de variables y funciones que veremos a continuación.
# 
# Cosas de lo más cotidianas como un perro o un coche pueden ser representadas con clases. Estas clases tienen diferentes características, que en el caso del perro podrían ser la edad, el nombre o la raza. Llamaremos a estas características, **atributos**.
# 
# Por otro lado, las clases tienen un conjunto de funcionalidades o cosas que pueden hacer. En el caso del perro podría ser andar o ladrar. Llamaremos a estas funcionalidades **métodos**.
# 
# Por último, pueden existir diferentes tipos de perro. Podemos tener uno que se llama Toby o el del vecino que se llama Laika. Llamaremos a estos diferentes tipos de perro **objetos**. Es decir, el concepto abstracto de perro es la clase, pero Toby o cualquier otro perro particular será el objeto.
# 
# La programación orientada a **objetos* está basada en 4 principios o pilares básicos:
# 
# **Herencia** <br>
# **Abstracción** <br>
# **Polimorfismo** <br>
# **Encapsulamiento** <br>
# 
# ## Objetivos
# *  Entender la estructura de POO en Python
# 

# # Definiendo clases
# 
# Vista ya la parte teórica, vamos a ver como podemos hacer uso de la programación orientada a objetos en Python. Lo primero es crear una clase, para ello usaremos el ejemplo de Alumno

# In[1]:


# Creando una clase vacía
class Alumno:
    pass


# Se trata de una clase vacía y sin mucha utilidad práctica, pero es la mínima clase que podemos crear. Nótese el uso del pass que no hace realmente nada, pero daría un error si después de los : no tenemos contenido.
# 
# Ahora que tenemos la **clase**, podemos crear un **objeto** de la misma. Podemos hacerlo como si de una variable normal se tratase. Nombre de la variable igual a la clase con (). Dentro de los paréntesis irían los parámetros de entrada si los hubiera.

# In[2]:


# Creamos un objeto de la clase Alumno
un_alumno = Alumno()


# # Definiendo atributos
# A continuación vamos a añadir algunos atributos a nuestra clase. Antes de nada es importante distinguir que existen dos tipos de atributos:
# 
# - Atributos de **instancia**: Pertenecen a la instancia de la clase o al objeto. Son atributos particulares de cada instancia, en nuestro caso de cada perro.
# - Atributos de **clase**: Se trata de atributos que pertenecen a la clase, por lo tanto serán comunes para todos los objetos.
# 
# Empecemos creando un par de atributos de instancia para nuestro alumno, el nombre y el grupo. Para ello creamos un método __init__ que será llamado automáticamente cuando creemos un objeto. Se trata del constructor.

# In[5]:


class Alumno:
    # El método __init__ es llamado al crear el objeto
    def __init__(self, nombre, grupo):
        print(f"Creando alumno {nombre}, {grupo}")

        # Atributos de instancia
        self.nombre = nombre
        self.grupo = grupo


# Ahora que hemos definido el método init con dos parámetros de entrada, podemos crear el objeto pasando el valor de los atributos. Usando type() podemos ver como efectivamente el objeto es de la clase **Alumno**.

# In[6]:


un_alumno = Alumno("Luis", "2-I")
print(type(un_alumno))
# Creando alumnno Luis, 2-I
# <class '__main__.Alumno'>


# Seguramente te hayas fijado en el **self** que se pasa como parámetro de entrada del método. Es una variable que representa la instancia de la clase, y deberá estar siempre ahí.
# El uso de __ init__ y el doble __ no es una coincidencia. Cuando veas un método con esa forma, significa que está reservado para un uso especial del lenguaje. En este caso sería lo que se conoce como **constructor**.
# 
# Por último, podemos acceder a los atributos usando el objeto y . (Punto) <br>
# 
# Por lo tanto.

# In[7]:


print(un_alumno.nombre) # Luis
print(un_alumno.grupo)   # 2-I


# Hasta ahora hemos definido atributos de instancia, ya que son atributos que pertenecen a cada alumno concreto. Ahora vamos a definir un atributo de clase, que será común para todos los alumnos. Por ejemplo, la escuela de los alumnos es algo común para todos los objetos **Alumno**

# In[8]:


class Alumno:
    # Atributo de clase
    escuela = 'CBTIS-246'

    # El método __init__ es llamado al crear el objeto
    def __init__(self, nombre, grupo):
        print(f"Creando alumno {nombre}, {grupo}")

        # Atributos de instancia
        self.nombre = nombre
        self.grupo = grupo


# Dado que es un atributo de clase, no es necesario crear un objeto para acceder al atributos. Podemos hacer lo siguiente.

# In[9]:


print(Alumno.escuela)
# CBTIS-246


# Se puede acceder también al atributo de clase desde el objeto.

# In[11]:


un_alumno = Alumno("Luis", "2-I")
un_alumno.escuela
# 'CBTIS-246'


# De esta manera, todos los objetos que se creen de la clase Alumno compartirán ese atributo de clase, ya que pertenecen a la misma.

# # Definiendo métodos
# En realidad cuando usamos **__ init__** anteriormente ya estábamos definiendo un método, solo que uno especial. A continuación vamos a ver como definir métodos que le den alguna funcionalidad interesante a nuestra clase, siguiendo con el ejemplo de alumno.
# 
# Vamos a codificar dos métodos, asistir y estudiar. El primero no recibirá ningún parámetro y el segundo recibirá el número de horas que queremos estudiar. Como hemos indicado anteriormente **self** hace referencia a la instancia de la clase. Se puede definir un método con **def** y el nombre, y entre **()** los parámetros de entrada que recibe, donde siempre tendrá que estar **self** el primero.

# In[13]:


class Alumno:
    # Atributo de clase
    escuela = 'CBTIS-246'

    # El método __init__ es llamado al crear el objeto
    def __init__(self, nombre, grupo):
        print(f"Creando alumno {nombre}, {grupo}")

        # Atributos de instancia
        self.nombre = nombre
        self.grupo = grupo

    def asistir(self):
        print("Asiste")

    def estudiar(self, horas):
        print(f"Estudiando {horas} horas")


# Por lo tanto si creamos un objeto un_alumno, podremos hacer uso de sus métodos llamándolos con . y el nombre del método. Como si de una función se tratase, pueden recibir y devolver argumentos.
# 

# In[14]:


un_alumno = Alumno("Juan", "2-J")
un_alumno.asistir()
un_alumno.estudiar(12)

# Creando alumno Juan, 2-J
# Asiste
# Estudia 12 horas


# # Métodos en Python: instancia, clase y estáticos
# En otros posts hemos visto como se pueden crear métodos con **def* dentro de una clase, pudiendo recibir parámetros como entrada y modificar el estado (como los atributos) de la instancia. Pues bien, haciendo uso de los decoradores, es posible crear diferentes tipos de métodos:
# 
# Lo métodos de instancia “normales” que ya hemos visto como **metodo()** <br>
# Métodos de clase usando el decorador **@classmethod** <br>
# Y métodos estáticos usando el decorador **@staticmethod** <br>
# En la siguiente clase tenemos un ejemplo donde definimos los tres tipos de métodos.

# In[15]:


class Clase:
    def metodo(self):
        return 'Método normal', self

    @classmethod
    def metododeclase(cls):
        return 'Método de clase', cls

    @staticmethod
    def metodoestatico():
        return "Método estático"


# Veamos su comportamiento en detalle uno por uno.
# 
# # Métodos de instancia
# Los métodos de instancia son los métodos normales, de toda la vida, que hemos visto anteriormente. Reciben como parámetro de entrada `self` que hace referencia a la instancia que llama al método. También pueden recibir otros argumentos como entrada.
# 
# **Para saber más*: El uso de `self`  es totalmente arbitrario. Se trata de una convención acordada por los usuarios de Python, usada para referirse a la instancia que llama al método, pero podría ser cualquier otro nombre. Lo mismo ocurre con `cls` , que veremos a continuación.

# In[16]:


class Clase:
    def metodo(self, arg1, arg2):
        return 'Método normal', self


# Y como ya sabemos, una vez creado un objeto pueden ser llamados.

# In[17]:


mi_clase = Clase()
mi_clase.metodo("a", "b")
# ('Método normal', <__main__.Clase at 0x10b9daa90>)


# En vista a esto, los métodos de instancia:
# 
# - Pueden **acceder y modificar los atributos del objeto.**
# - Pueden **acceder a otros métodos.**
# - Dado que desde el objeto self se puede acceder a la clase con `self.class`, también pueden **modificar el estado de la clase**.

# # Métodos de clase (classmethod)
# A diferencia de los métodos de instancia, los métodos de clase reciben como argumento `cls`, que hace referencia a la clase. Por lo tanto, pueden acceder a la clase pero no a la instancia.

# In[18]:


class Clase:
    @classmethod
    def metododeclase(cls):
        return 'Método de clase', cls


# Se pueden llamar sobre la clase.

# In[ ]:


Clase.metododeclase()
# ('Método de clase', __main__.Clase)


# Pero también se pueden llamar sobre el objeto.

# In[ ]:


mi_clase.metododeclase()
# ('Método de clase', __main__.Clase)


# Por lo tanto, los **métodos de clase**:
# 
# **No** pueden acceder a los atributos de la instancia. <br>
# Pero **si pueden** modificar los atributos de la clase

# # Métodos estáticos (staticmethod)
# Por último, los métodos estáticos se pueden definir con el decorador @staticmethod y no aceptan como parámetro ni la instancia ni la clase. Es por ello por lo que **no pueden modificar el estado ni de la clase ni de la instancia.** Pero por supuesto pueden aceptar parámetros de entrada.

# In[20]:


class Clase:
    @staticmethod
    def metodoestatico():
        return "Método estático"


# In[21]:


mi_clase = Clase()
Clase.metodoestatico()
mi_clase.metodoestatico()

# 'Método estático'
# 'Método estático'


# Por lo tanto el uso de los **métodos estáticos** pueden resultar útil para indicar que un método no modificará el estado de la instancia ni de la clase. Es cierto que se podría hacer lo mismo con un método de instancia por ejemplo, pero a veces resulta importante indicar de alguna manera estas peculiaridades, evitando así futuros problemas y malentendidos.
# 
# En otras palabras, los métodos estáticos se podrían ver como funciones normales, con la salvedad de que van ligadas a una clase concreta.

# # Herencia en Python
# Para entender la herencia, es fundamental entender la programación orientada a objetos, por lo que te recomendamos empezar por ahí antes.
# 
# La **herencia** es un proceso mediante el cual se puede crear una clase **hija** que hereda de una clase **padre**, compartiendo sus métodos y atributos. Además de ello, una clase hija puede sobreescribir los métodos o atributos, o incluso definir unos nuevos.
# 
# Se puede crear una clase hija con tan solo pasar como parámetro la clase de la que queremos heredar. En el siguiente ejemplo vemos como se puede usar la herencia en Python, con la clase `Alumno` que hereda de `Humano`. 
# 

# In[25]:


# Definimos una clase padre
class Humano:
    pass

# Creamos una clase hija que hereda de la padre
class Alumno(Humano):
    pass


# De hecho podemos ver como efectivamente la clase **Alumno** es la hija de **Humano** usando `__ bases__`

# In[26]:


print(Alumno.__bases__)
# (<class '__main__.Humano'>,)


# De manera similar podemos ver que clases descienden de una en concreto con `__ subclasses__`.

# In[27]:


print(Alumno.__subclasses__())
# [<class '__main__.Humano'>]


# **¿Para que necesitamos la herencia?** Dado que una clase hija hereda los atributos y métodos de la padre, nos puede ser muy útil cuando tengamos clases que se parecen entre sí pero tienen ciertas particularidades. En este caso en vez de definir un montón de clases para cada animal, podemos tomar los elementos comunes y crear una clase Alumno de la que hereden el resto, respetando por tanto la filosofía `DRY`. Realizar estas abstracciones y buscar el denominador común para definir una clase de la que hereden las demás, es una tarea de lo más compleja en el mundo de la programación.
# 
# **Para saber más**: El principio `DRY` (Don't Repeat Yourself) es muy aplicado en el mundo de la programación y consiste en no repetir código de manera innecesaria. Cuanto más código duplicado exista, más difícil será de modificar y más fácil será crear inconsistencias. Las clases y la herencia a no repetir código.

# # Extendiendo y modificando métodos
# Continuemos con nuestro ejemplo de alumnos y humanos. Vamos a definir una clase padre Alumno que tendrá todos los atributos y métodos genéricos que los humanos pueden tener. Esta tarea de buscar el denominador común es muy importante en programación. Veamos los atributos:
# 
# - Tenemos la **estatura** ya que todos los humanos tienen una.
# - Y la **edad**, ya que todo ser vivo nace, crece, se reproduce y muere.
#   
# Y los métodos o funcionalidades:
# 
# - Tendremos el método **hablar**, que cada humano implementará de una forma.
# - Un método **moverse**. Unos humanos lo harán caminando, otros en auto.
# - Y por último un método **descríbeme** que será común.
#   
# Definimos la clase padre, con una serie de atributos comunes para todos los humanos como hemos indicado.

# In[31]:


class Humano:
    def __init__(self, estatura, edad):
        self.estatura = estatura
        self.edad = edad

    # Método genérico pero con implementación particular
    def hablar(self):
        # Método vacío
        pass

    # Método genérico pero con implementación particular
    def moverse(self):
        # Método vacío
        pass

    # Método genérico con la misma implementación
    def describeme(self):
        print("Soy un Humano del tipo", type(self).__name__)


# Tenemos ya por lo tanto una clase genérica `Alumno`, que generaliza las características y funcionalidades que todo humano puede tener. Ahora creamos una clase `Alumno` que hereda del `Humano`. Como primer ejemplo vamos a crear una clase vacía, para ver como los métodos y atributos son heredados por defecto.

# In[33]:


# Alumno hereda de Humano
class Alumno(Humano):
    pass

un_alumno = Alumno(168, 16)
un_alumno.describeme()
# Soy un Humano del tipo Alumno


# Con tan solo un par de líneas de código, hemos creado una clase nueva que tiene todo el contenido que la clase padre tiene, pero aquí viene lo que es de verdad interesante. Vamos a crear varios alumnos concretos y sobreescrbir algunos de los métodos que habían sido definidos en la clase `Alumno`, como el `hablar` o el `moverse`, ya que cada alumno se comporta de una manera distinta.
# 
# Podemos incluso crear nuevos métodos que se añadirán a los ya heredados, como en el caso de la `Director` con `evaluar()`.

# In[38]:


class Alumno(Humano):
    def hablar(self):
        print("Hola")
    def moverse(self):
        print("Leegando en un Mercedez de 40 pasajeros")

class Profesor(Humano):
    def hablar(self):
        print("Su tarea?")
    def moverse(self):
        print("Llegando en un Ford Fiesta")

class Director(Humano):
    def hablar(self):
        print("Apoyense los unos a los otros")
    def moverse(self):
        print("Usando un KIA SUV")

    # Nuevo método
    def evaluar(self):
        print("¿Como va todo?")


# Por lo tanto ya podemos crear nuestros objetos de esos animales y hacer uso de sus métodos que podrían clasificarse en tres:
# 
# - Heredados directamente de la clase padre: `describeme()`
# - Heredados de la clase padre pero modificados: `hablar()` y `moverse()`
# - Creados en la clase hija por lo tanto no existentes en la clase padre: `evaluar()`

# In[40]:


un_alumno = Alumno(168, 10)
un_profesor = Profesor(190, 23)
un_director = Director(185, 1)

un_alumno.hablar()
un_profesor.hablar()
# Hola
# Su tarea?

un_profesor.describeme()
un_director.describeme()
# Soy un Humano del tipo Profesor
# Soy un Animal del tipo Abeja

un_director.evaluar()
# ¿Como va todo?


# # Uso de super()
# En pocas palabras, la función `super()` nos permite acceder a los métodos de la clase padre desde una de sus hijas. Volvamos al ejemplo de `Humano` y `Alumno`.

# In[48]:


class Humano:
    def __init__(self, estatura, edad):
        self.estatura = estatura
        self.edad = edad        
    def hablar(self):
        pass

    def moverse(self):
        pass

    def describeme(self):
        print("Soy un Humano del tipo", type(self).__name__)


# Tal vez queramos que nuestro Alumno tenga un parámetro extra en el constructor, como podría ser el codigo. Para realizar esto tenemos dos alternativas:
# 
# Podemos crear un nuevo `__init__` y guardar todas las variables una a una.
# O podemos usar **super()** para llamar al `__init__` de la clase padre que ya aceptaba la **estatura** y **edad**, y sólo asignar la variable nueva manualmente.

# In[49]:


class Alumno(Humano):
    def __init__(self, estatura, edad, codigo):
        # Alternativa 1
        # self.estatura = estatura
        # self.edad = edad
        # self.codigo = codigo

        # Alternativa 2
        super().__init__(estatura, edad)
        self.codigo = codigo


# In[50]:


un_alumno = Alumno(166, 7, 'ALM001')
un_alumno.estatura
un_alumno.edad
un_alumno.codigo


# # Herencia múltiple
# En Python es posible realizar **herencia múltiple**. En otros posts hemos visto como se podía crear una clase padre que heredaba de una clase hija, pudiendo hacer uso de sus métodos y atributos. La herencia múltiple es similar, pero una clase **hereda de varias clases** padre en vez de una sola.
# 
# Veamos un ejemplo. Por un lado tenemos dos clases `Clase1` y `Clase2`, y por otro tenemos la `Clase3` que hereda de las dos anteriores. Por lo tanto, heredará todos los métodos y atributos de ambas.

# In[51]:


class Clase1:
    pass
class Clase2:
    pass
class Clase3(Clase1, Clase2):
    pass


# Es posible también que una clase herede de otra clase y a su vez otra clase herede de la anterior.

# In[52]:


class Clase1:
    pass
class Clase2(Clase1):
    pass
class Clase3(Clase2):
    pass


# Llegados a este punto nos podemos plantear lo siguiente. Vale, como sabemos de otros posts las clases hijas heredan los métodos de las clases padre, pero también pueden reimplementarlos de manera distinta. Entonces, si llamo a un método que todas las clases tienen en común ¿a cuál se llama?. Pues bien, existe una forma de saberlo.
# 
# La forma de saber a que método se llama es consultar el *MRO* o Method Order Resolution. Esta función nos devuelve una tupla con el orden de búsqueda de los métodos. Como era de esperar se empieza en la propia clase y se va subiendo hasta la clase padre, de izquierda a derecha.

# In[53]:


class Clase1:
    pass
class Clase2:
    pass
class Clase3(Clase1, Clase2):
    pass

print(Clase3.__mro__)
# (<class '__main__.Clase3'>, <class '__main__.Clase1'>, <class '__main__.Clase2'>, <class 'object'>)


# Una curiosidad es que al final del todo vemos la clase `object`. Aunque pueda parecer raro, es correcto ya que en realidad todas las clases en Python heredan de una clase genérica object, aunque no lo especifiquemos explícitamente.
# 
# Y como último ejemplo,…el cielo es el límite. Podemos tener una clase heredando de otras tres. <br>
# Fíjate en que el **MRO** depende del orden en el que las clases son pasadas: 1, 3, 2.

# In[54]:


class Clase1:
    pass
class Clase2:
    pass
class Clase3:
    pass
class Clase4(Clase1, Clase3, Clase2):
    pass
print(Clase4.__mro__)
# (<class '__main__.Clase4'>, <class '__main__.Clase1'>, <class '__main__.Clase3'>, <class '__main__.Clase2'>, <class 'object'>)


# Y como ya sabemos, una vez creado un objeto pueden ser llamados.

# # Abstracción en programación
# La abstracción es un termino que hace referencia a la ocultación de la complejidad intrínseca de una aplicación al exterior, centrándose sólo en como puede ser usada, lo que se conoce como **interfaz**. Si has oído hablar del enfoque **caja negra**, es un concepto muy relacionado. Dicho en otras palabras, la abstracción consiste en ocultar toda la complejidad que algo puede tener por dentro, ofreciéndonos unas funciones de alto nivel, por lo general sencillas de usar, que pueden ser usadas para interactuar con la aplicación sin tener conocimiento de lo que hay dentro.
# 
# Una analogía del mundo real podría ser la televisión. Se trata de un dispositivo muy complejo donde han trabajado gran cantidad de ingenieros de diversas disciplinas como telecomunicaciones o electrónica. ¿Os imagináis que para cambiar de canal tuviéramos que saber todos los entresijos del aparato?. Pues bien, se nos ofrece una abstracción de la televisión, un **mando a distancia**. El mando nos abstrae por completo de la complejidad de los circuitos y señales, y nos da una interfaz sencilla que con unos pocos botones podemos usar.
# 
# Algo muy parecido sucede en la programación orientada a objetos. Si tuviéramos una clase `Avion`, en su interior podría haber líneas y líneas de código super complejas, pero una buena abstracción sería la que simplemente ofreciera los métodos `encender()`, `apagar()` y `aterrizar()` al exterior.
# 
# Un concepto relacionado con la abstracción, serían las clases abstractas o más bien los métodos abstractos. Se define como clase abstracta la que contiene métodos abstractos, y se define como método abstracto a un método que ha sido declarado pero no implementado. Es decir, que no tiene código.
# 
# Es posible crear métodos abstractos en Python con decoradores como @absttractmethod, pero esto lo dejamos para otro post.

# # Polimorfismo en Python
# El término polimorfismo visto desde el punto de vista de Python es complicado de explicar sin hablar del duck typing, por lo que te recomendamos la lectura.
# 
# Al ser un lenguaje con tipado dinámico y permitir duck typing, en Python no es necesario que los objetos compartan un interfaz, simplemente basta con que tengan los métodos que se quieren llamar.
# 
# Podemos recrear el ejemplo de Java de la siguiente manera. Supongamos que tenemos un clase Animal con un método hablar().

# In[4]:


class Humano:
    def hablar(self):
        pass


# Por otro lado tenemos otras dos clases, `Ingles`, `Mexicano` que heredan de la anterior. Además, implementan el método hablar() de una forma distinta.

# In[5]:


class Ingles(Humano):
    def hablar(self):
        print("Hello!")

class Mexicano(Humano):
    def hablar(self):
        print("Hola!")


# A continuación creamos un objeto de cada clase y llamamos al método `hablar()`. Podemos observar que cada humano se comporta de manera distinta al usar hablar().

# In[6]:


for humano in Mexicano(), Ingles():
    humano.hablar()


# En el caso anterior, la variable humano ha ido “tomando las formas” de `Ingles` y `Mexicano`. Sin embargo, nótese que al tener tipado dinámico este ejemplo hubiera funcionado igual sin que existiera herencia entre Mexicano e Ingles, pero esta explicación la dejamos para el capítulo de duck typing

# # Encapsulamiento en programación
# El encapsulamiento o encapsulación en programación es un concepto relacionado con la programación orientada a objetos, y hace referencia al ocultamiento de los estado internos de una clase al exterior. Dicho de otra manera, encapsular consiste en hacer que los atributos o métodos internos a una clase no se puedan acceder ni modificar desde fuera, sino que tan solo el propio objeto pueda acceder a ellos.
# 
# Para la gente que conozca Java, le resultará un termino muy familiar, pero en Python es algo distinto. Digamos que Python por defecto no oculta los atributos y métodos de una clase al exterior. Veamos un ejemplo con el lenguaje Python.

# In[7]:


class Clase:
    atributo_clase = "Hola"
    def __init__(self, atributo_instancia):
        self.atributo_instancia = atributo_instancia

mi_clase = Clase("Que tal")
mi_clase.atributo_clase
mi_clase.atributo_instancia

# 'Hola'
# 'Que tal'


# Ambos atributos son perfectamente accesibles desde el exterior. Sin embargo esto es algo que tal vez no queramos. Hay ciertos métodos o atributos que queremos que pertenezcan sólo a la clase o al objeto, y que sólo puedan ser accedidos por los mismos. Para ello podemos usar la doble __ para nombrar a un atributo o método. Esto hará que Python los interprete como “privados”, de manera que no podrán ser accedidos desde el exterior.

# In[8]:


class Clase:
    atributo_clase = "Hola"   # Accesible desde el exterior
    __atributo_clase = "Hola" # No accesible

    # No accesible desde el exterior
    def __mi_metodo(self):
        print("Haz algo")
        self.__variable = 0

    # Accesible desde el exterior
    def metodo_normal(self):
        # El método si es accesible desde el interior
        self.__mi_metodo()

mi_clase = Clase()
#mi_clase.__atributo_clase  # Error! El atributo no es accesible
#mi_clase.__mi_metodo()     # Error! El método no es accesible
mi_clase.atributo_clase     # Ok!
mi_clase.metodo_normal()    # Ok!


# Y como curiosidad, podemos hacer uso de `dir` para ver el listado de métodos y atributos de nuestra clase. Podemos ver claramente como tenemos el `metodo_normal` y el `atributo` de clase, pero no podemos encontrar `__mi_metodo` ni `__atributo_clase`.

# In[9]:


print(dir(mi_clase))
#['_Clase__atributo_clase', '_Clase__mi_metodo', '_Clase__variable',
#'__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__',
#'__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__',
#'__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__',
#'__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__',
#'__str__', '__subclasshook__', '__weakref__', 'atributo_clase', 'metodo_normal']


# Pues bien, en realidad si que podríamos acceder a `__atributo_clase` y a `__mi_metodo` haciendo un poco de trampa. Aunque no se vea a simple vista, si que están pero con un nombre distinto, para de alguna manera ocultarlos y evitar su uso. Pero podemos llamarlos de la siguiente manera, pero por lo general **no es una buena idea**.

# # Excepciones en Python
# Las excepciones en Python son una herramienta muy potente que la gran mayoría de lenguajes de programación modernos tienen. Se trata de una **forma de controlar el comportamiento de un programa cuando se produce un error**.
# 
# Esto es muy importante ya que salvo que tratemos este error, el **programa se parará**, y esto es algo que en determinadas aplicaciones no es una opción válida.
# 
# Imaginemos que tenemos el siguiente código con dos variables a y b y realizamos su división `a/b`.

# In[10]:


a = 4
b = 2
c = a/b


# Pero imaginemos ahora que por cualquier motivo las variables tienen otro valor, y que por ejemplo `b` tiene el valor `0`. Si intentamos hacer la división entre cero, este **programa dará un error** y su ejecución terminará de manera abrupta.

# In[11]:


a = 4; b = 0
print(a/b)
# ZeroDivisionError: division by zero


# Ese **“error”** que decimos que ha ocurrido es lanzado por Python (raise en Inglés) ya que la división entre cero es una operación que matemáticamente no está definida.
# 
# Se trata de la excepción `ZeroDivisionError`. En el siguiente enlace, tenemos un listado de todas las excepciones con las que nos podemos encontrar.
# 
# Veamos un ejemplo con otra excepción. ¿Que pasaría si intentásemos sumar un número con un texto? Evidentemente esto no tiene ningún sentido, y Python define una excepción para esto llamada `TypeError`.

# In[13]:


print(2 + "2")


# En base a esto es muy **importante controlar las excepciones**, porque por muchas comprobaciones que realicemos es posible que en algún momento ocurra una, y si no se hace nada el **programa se parará**.
# 
# ¿Te imaginas que en un avión, un tren o un cajero automático tiene un error que lanza raise una excepción y se detiene por completo?
# 
# Una primera aproximación al control de excepciones podría ser el siguiente ejemplo. Podemos realizar una comprobación manual de que no estamos dividiendo por cero, para así evitar tener un error tipo `ZeroDivisionError`.
# 
# Sin embargo es complicado escribir código que contemple y que prevenga todo tipo de excepciones. Para ello, veremos más adelante el uso de `except`.

# In[14]:


a = 5
b = 0
# A través de esta comprobación prevenimos que se divida entre cero.
if b!=0:
    print(a/b)
else:
    print("No se puede dividir!")


# # Uso de raise
# También podemos ser nosotros los que levantemos o lancemos una excepción. Volviendo a los ejemplos usados en el apartado anterior, **podemos ser nosotros los que levantemos** `ZeroDivisionError` o `NameError` usando `raise`. La sintaxis es muy fácil.

# In[ ]:


raise ZeroDivisionError("Información de la excepción")


# O podemos lanzar otra de tipo  `NameError`.

# In[ ]:


raise NameError("Información de la excepción")


# Se puede ver como el `string` que hemos pasado se imprime a continuación de la excepción. Se puede llamar también sin ningún parámetro como se hace a continuación.

# In[16]:


raise ZeroDivisionError


# Visto esto, ya sabemos como una excepción puede ser lanzada. Existen dos maneras principalmente:
# 
# - Hacemos una operación que no puede ser realizada (como dividir por cero). En este caso Python se encarga de lanzar automáticamente la excepción.
# - O también podemos lanzar nosotros una excepción manualmente, usando `raise`.
# - Habría un tercer caso que sería lanzar una excepción que no pertenece a las definidas por defecto en Python. A continuación veremos que podemos hacer para controlar estas excepciones, y que hacer cuando se lanza una para que no se interrumpa la ejecución del programa.

# # Uso de try y except
# La buena noticia es que las excepciones que hemos visto antes, **pueden ser capturadas** y manejadas adecuadamente, **sin que el programa se detenga**. Veamos un ejemplo con la división entre cero.

# In[ ]:


a = 5; b = 0
try:
    c = a/b
except ZeroDivisionError:
    print("No se ha podido realizar la división")


# En este caso no verificamos que `b!=0`. Directamente intentamos realizar la división y en el caso de que se lance la excepción `ZeroDivisionError`, la capturamos y la tratamos adecuadamente.
# 
# La diferencia con el ejemplo anterior es que ahora no se para el programa y se puede seguir ejecutando. Prueba a ejecutar el código y ver que pasa. Verás como el programa ya no se para.
# 
# Entonces, lo que hay dentro del `try` es la sección del código que podría lanzar la excepción que se está capturando en el `except`. Por lo tanto cuando ocurra una excepción, se entra en el `except` pero el **programa no se para**.
# 
# 
# 
# También se puede capturar diferentes excepciones como se ve en el siguiente ejemplo.

# In[ ]:


try:
    #c = 5/0       # Si comentas esto entra en TypeError
    d = 2 + "Hola" # Si comentas esto entra en ZeroDivisionError
except ZeroDivisionError:
    print("No se puede dividir entre cero!")
except TypeError:
    print("Problema de tipos!")


# Puedes también hacer que un determinado número de excepciones se traten de la misma manera con el mismo bloque de código. Sin embargo suele ser más interesante tratar a diferentes excepciones de diference manera.

# In[ ]:


try:
    #c = 5/0       # Si comentas esto entra en TypeError
    d = 2 + "Hola" # Si comentas esto entra en ZeroDivisionError
except (ZeroDivisionError, TypeError):
    print("Excepcion ZeroDivisionError/TypeError")


# Otra forma si no sabes que excepción puede saltar, puedes usar la clase genérica `Exception`. En este caso se controla cualquier tipo de excepción. De hecho todas las excepciones heredan de `Exception`. 

# In[ ]:


try:
    #c = 5/0       # Si comentas esto entra en TypeError
    d = 2 + "Hola" # Si comentas esto entra en ZeroDivisionError
except Exception:
    print("Ha habido una excepción")


# No obstante hay una forma de saber que excepción ha sido la que ha ocurrido.

# In[ ]:


try:
    d = 2 + "Hola" # Si comentas esto entra en ZeroDivisionError
except Exception as ex:
    print("Ha habido una excepción", type(ex))

# Ha habido una excepción <class 'TypeError'>


# # Uso de else
# Al ya explicado `try` y `except` le podemos añadir un bloque más, el `else`. Dicho bloque **se ejecutará si no ha ocurrido ninguna excepción**. Fíjate en la diferencia entre los siguientes códigos.

# In[ ]:


try:
    # Forzamos una excepción al dividir entre 0
    x = 2/0
except:
    print("Entra en except, ha ocurrido una excepción")
else:
    print("Entra en else, no ha ocurrido ninguna excepción")

#Entra en except, ha ocurrido una excepción


# Sin embargo en el siguiente código la división se puede realizar sin problema, por lo que el bloque except no se ejecuta pero el else si es ejecutado.

# In[17]:


try:
    # La división puede realizarse sin problema
    x = 2/2
except:
    print("Entra en except, ha ocurrido una excepción")
else:
    print("Entra en else, no ha ocurrido ninguna excepción")

#Entra en else, no ha ocurrido ninguna excepción


# # Uso de finally
# A los ya vistos bloques `try`, `except` y `else` podemos añadir un bloque más, el `finally`. Dicho bloque se **ejecuta siempre**, haya o no haya habido excepción.
# 
# Este bloque se suele usar si queremos ejecutar algún tipo de **acción de limpieza**. Si por ejemplo estamos escribiendo datos en un fichero pero ocurre una excepción, tal vez queramos borrar el contenido que hemos escrito con anterioridad, para no dejar datos inconsistenes en el fichero.
# 
# 
# 
# En el siguiente código vemos un ejemplo. Haya o no haya excepción el código que haya dentro de finally será ejecutado.

# In[ ]:


try:
    # Forzamos excepción
    x = 2/0
except:
    # Se entra ya que ha habido una excepción
    print("Entra en except, ha ocurrido una excepción")
finally:
    # También entra porque finally es ejecutado siempre
    print("Entra en finally, se ejecuta el bloque finally")

#Entra en except, ha ocurrido una excepción
#Entra en finally, se ejecuta el bloque finally


# # Ejemplos
# Un ejemplo muy típico de excepciones es en el **manejo de ficheros**. Se intenta abrir, pero se captura una posible excepción. De hecho si entras en la documentación de open se indica que `OSError` es lanzada si el fichero no puede ser abierto.

# In[ ]:


# Se intenta abrir un fichero y se captura una posible excepción
try:
    with open('fichero.txt') as file:
        read_data = file.read()
except:
    # Se entra aquí si no pudo ser abierto
    print('No se pudo abrir')


# Como ya hemos comentado, en el `except` también se puede capturar una excepción concreta. Dependiendo de nuestro programa, tal vez queramos tratar de manera distinta diferentes tipos de excepciones, por lo que es una buena práctica especificar que tipo de excepción estamos tratando.

# In[ ]:


# Se intenta abrir un fichero y se captura una posible excepción
try:
    with open('fichero.txt') as file:
        read_data = file.read()
# Capturamos una excepción concreta
except OSError:
    print('OSError. No se pudo abrir')


# En este otro ejemplo vemos el uso de los bloques `try`, `except`, `else` y `finally` todos juntos.

# In[ ]:


try:
    # Se fuerza excepción
    x = 2/0
except:
    print("Entra en except, ha ocurrido una excepción")
else:
    print("Entra en el else, no ha ocurrido ninguna excepción")
finally:
    print("Entra en finally, se ejecuta el bloque finally")


# También se puede capturar una excepción de tipo  `SyntaxError`, que hace referencia a errores de sintaxis. Sin embargo el código debería estar libre de este tipo de fallos, por lo que tal vez nunca deberías usar esto.

# In[ ]:


try:
    print("Hola"))
except SyntaxError:
    print("Hay un error de sintaxis")


# # Leer archivos en Python
# Al igual que en otros lenguajes de programación, en Python es posible **abrir ficheros y leer su contenido**. Los ficheros o archivos pueden ser de lo más variado, desde un simple texto a contenido binario. Para simplificar nos centraremos en **leer un fichero de texto**
# 
# Imagínate entonces que tienes un fichero de texto con unos datos, como podría ser un `.txt` o un `.csv`, y quieres leer su contenido para realizar algún tipo de procesado sobre el mismo. Nuestro fichero podría ser el siguiente.

# In[ ]:


# contenido del fichero ejemplo.txt
Contenido de la primera línea
Contenido de la segunda línea
Contenido de la tercera línea
Contenido de la cuarta línea


# Podemos abrir el fichero con la función `open()` pasando como argumento el nombre del fichero que queremos abrir.

# In[ ]:


fichero = open('ejemplo.txt')


# # Método `read()`
# Con `open()` tendremos ya en `fichero` el contenido del documento listo para usar, y podemos imprimir su contenido con `read()`. El siguiente código imprime **todo el fichero**.

# In[ ]:


print(fichero.read())
#Contenido de la primera línea
#Contenido de la segunda línea
#Contenido de la tercera línea
#Contenido de la cuarta línea


# # Método `readline()`
# Es posible también leer un **número de líneas determinado** y no todo el fichero de golpe. Para ello hacemos uso de la función `readline()`. Cada vez que se llama a la función, se lee una línea.

# In[ ]:


fichero = open('ejemplo.txt')
print(fichero.readline())
print(fichero.readline())
# Contenido de la primera línea
# Contenido de la segunda línea


# Es muy **importante saber** que una vez hayas leído todas las línea del archivo, la función ya no devolverá nada, porque se habrá llegado al final. Si quieres que `readline()` funcione otra vez, podrías por ejemplo volver a leer el fichero con `open()`.
# 
# Otra forma de usar `readline()` es pasando como argumento un número. Este número leerá un **determinado número de caracteres**. El siguiente código lee todo el fichero carácter por carácter.

# In[ ]:


fichero = open('ejemplo.txt')
caracter = fichero.readline(1)
while caracter != "":
    #print(caracter)
    caracter = fichero.readline(1)


# # Método `readlines()`
# 
# Existe otro método llamado `readlines()`, que devuelve una lista donde **cada elemento es una línea del fichero**.

# In[ ]:


fichero = open('ejemplo.txt')
lineas = fichero.readlines()
print(lineas)
#['Contenido de la primera línea\n', 'Contenido de la segunda línea\n',
#'Contenido de la tercera línea\n', 'Contenido de la cuarta línea']


# De manera muy sencilla podemos iterar las líneas e imprimirlas por pantalla.

# In[ ]:


fichero = open('ejemplo.txt')
lineas = fichero.readlines()
for linea in lineas:
    print(linea)
#Contenido de la primera línea
#Contenido de la segunda línea
#Contenido de la tercera línea
#Contenido de la cuarta línea


# # Argumentos de `open()`
# Hasta ahora hemos visto la función `open()` con tan sólo un argumento de entrada, el nombre del fichero. Lo cierto es que existe un segundo argumento que es importante especificar. Se trata del **modo de apertura del fichero**. En la documentación oficial se explica en detalle.
# 
# - ‘r’: Por defecto, para leer el fichero.
# - ‘w’: Para escribir en el fichero.
# - ‘x’: Para la creación, fallando si ya existe.
# - ‘a’: Para añadir contenido a un fichero existente.
# - ‘b’: Para abrir en modo binario.
#   
# Por lo tanto lo estrictamete correcto si queremos leer el fichero sería hacer lo siguiente. Aunque el modo r sea por defecto, es una buena práctica indicarlo para darle a entender a otras personas que lean nuestro código que no queremos modificarlo, tan solo leerlo.

# In[ ]:


fichero = open('ejemplo.txt', 'r')


# # Cerrando el fichero
# 
# Otra cosa que debemos hacer cuando trabajamos con ficheros en Python, es **cerrarlos una vez que ya hemos acabado con ellos**. Aunque es verdad que el fichero normalmente acabará siendo cerrado automáticamente, es importante especificarlo para evitar tener comportamientos inesperados.
# 
# Por lo tanto si queremos cerrar un fichero sólo tenemos que usar la función close() sobre el mismo. Por lo tanto tenemos tres pasos:
# 
# - Abrir el fichero que queramos. En modo texto usaremos ‘r’.
# - Usar el fichero para recopilar o procesar los datos que necesitábamos.
# - Cuando hayamos acabado, cerramos el fichero.

# In[ ]:


fichero = open('ejemplo.txt', 'r')
# Usar la variable fichero
# Cerrar el fichero
fichero.close()


# Existen otras formas de hacerlo, como con el uso de **excepciones** que veremos en otros posts. Un ejemplo sería el siguiente. No pasa nada si aún no entiendes el uso del `try` y `finally`, por ahora quédate con que la sección `finally` **se ejecuta siempre** sin importar si hay un error o no. De esta manera el `close()` siempre será ejecutado.

# In[ ]:


fichero = open('ejemplo.txt')
try:
    # Usar el fichero
    pass
finally:
    # Esta sección es siempre ejecutada
    fichero.close()


# Y por si no fuera poco, existe otra forma de cerrar el fichero automáticamente. Si hacemos uso se `with()`, el fichero **se cerrará automáticamente una vez se salga de ese bloque de código**.

# In[ ]:


with open('ejemplo.txt') as fichero:
    # Usar el fichero. Se cerrará automáticamente
    pass


# # Ejemplos
# Como ya hemos visto `readline()` lee línea por línea el fichero. También hacemos uso de un bucle while para leer líneas mientras que no se haya llegado al final. Es por eso por lo que comparamos `linea != ''`, ya que se devuelve un string vació cuando se ha llegado al final.

# In[ ]:


with open('ejemplo.txt', 'r') as fichero:
    linea = fichero.readline()
    while linea != '':
        print(linea, end='')
        linea = fichero.readline()

#Contenido de la primera línea
#Contenido de la segunda línea
#Contenido de la tercera línea
#Contenido de la cuarta línea


# Nos podemos ahorrar alguna línea de código si hacemos lo siguiente, ya que `readlines()` nos devuelve directamente una lista que podemos iterar con las líneas.

# In[ ]:


with open('ejemplo.txt', 'r') as fichero:
    for linea in fichero.readlines():
        print(linea, end='')
#Contenido de la primera línea
#Contenido de la segunda línea
#Contenido de la tercera línea
#Contenido de la cuarta línea


# Pero puede ser simplificado aún más de la siguiente manera. Nótese que usamos el `end=''` para decirle a Python que no imprima el salto de línea `\n` al final del print.

# In[ ]:


with open('ejemplo.txt', 'r') as fichero:
    for linea in fichero:
        print(linea, end='')
#Contenido de la primera línea
#Contenido de la segunda línea
#Contenido de la tercera línea
#Contenido de la cuarta línea


# # Escribir archivos en Python
# A continuación te explicamos **como escribir datos en un fichero usando Python**. Imagínate que tienes unos datos que te gustaría guardar en un fichero para su posterior análisis. Te explicamos como guardarlos en un fichero, por ejemplo, `.txt`.
# 
# Lo primero que debemos de hacer es crear un objeto para el fichero, con el nombre que queramos. Al igual que vimos en el post de leer ficheros, además del nombre se puede pasar un segundo parámetro que indica el modo en el que se tratará el fichero. Los más relevantes en este caso son los siguientes. Para más información consulta la documentación oficial.
# 
# - ‘w’: Borra el fichero si ya existiese y crea uno nuevo con el nombre indicado.
# - ‘a’: Añadirá el contenido al final del fichero si ya existiese (append end Inglés)
# - ‘x’: Si ya existe el fichero se devuelve un error.
#   
# Por lo tanto con la siguiente línea estamos creando un fichero con el nombre datos_guardados.txt.

# In[ ]:


# Abre un nuevo fichero
fichero = open("datos_guardados.txt", 'w')


# Si por lo contrario queremos añadir el contenido al ya existente en un fichero de antes, podemos hacerlo en el modo append como hemos indicado.

# In[ ]:


# Abre un nuevo y añade el contenido al final
fichero = open("datos_guardados.txt", 'a')


# # Método `write()`
# Ya hemos visto como crear el fichero. Veamos ahora como podemos añadir contenido. Empecemos escribiendo un texto.

# In[ ]:


fichero = open("datos_guardados.txt", 'w')
fichero.write("Contenido a escribir")
fichero.close()


# Por lo tanto si ahora abrimos el fichero `datos_guardados.txt`, veremos como efectivamente contiene una línea con Contenido a escribir. ¿A que es fácil?
# 
# Es **muy importante** el uso de `close()` ya que si dejamos el fichero abierto, podríamos llegar a tener un comportamiento inesperado que queremos evitar. Por lo tanto, siempre que se abre un fichero es **necesario cerrarlo** cuando hayamos acabado.
# 
# Compliquemos un poco más las cosas. Ahora vamos a guardar una lista de elementos en el fichero, donde cada elemento de la lista se almacenará en una línea distinta.

# In[ ]:


# Abrimos el fichero
fichero = open("datos_guardados.txt", 'w')

# Tenemos unos datos que queremos guardar
lista = ["Manzana", "Pera", "Plátano"]

# Guardamos la lista en el fichero
for linea in lista:
    fichero.write(linea + "\n")

# Cerramos el fichero
fichero.close()


# Si te fijas, estamos almacenando la línea mas `\n`. Es importante añadir el salto de línea porque por defecto no se añade, y si queremos que cada elemento de la lista se almacena en una línea distinta, será necesario su uso.

# # Método `writelines()`
# También podemos usar el método `writelines()` y pasarle una lista. Dicho método se encargará de guardar todos los elementos de la lista en el fichero.

# In[ ]:


fichero = open("datos_guardados.txt", 'w')
lista = ["Manzana", "Pera", "Plátano"]

fichero.writelines(lista)
fichero.close()

# Se guarda
# ManzanaPeraPlátano


# Tal vez te hayas dado cuenta de que en realidad lo que se guarda es ManzanaPeraPlátano, todo junto. Si queremos que cada elemento se almacene en una línea distinta, deberíamos añadir el salto de línea en cada elemento de la lista como se muestra a continuación.

# In[ ]:


fichero = open("datos_guardados.txt", 'w')
lista = ["Manzana\n", "Pera\n", "Plátano\n"]

fichero.writelines(lista)
fichero.close()

# Se guarda
# Manzana
# Pera
# Plátano


# # Uso del `with`
# Podemos ahorrar una línea de código si hacemos uso de lo siguiente. En este caso nos podemos ahorrar la llamada al close() ya que se realiza automáticamente. El código anterior se podría reescribir de la siguiente manera.

# In[ ]:


lista = ["Manzana\n", "Pera\n", "Plátano\n"]
with open("datos_guardados.txt", 'w') as fichero:
     fichero.writelines(lista)


# # Ejemplos escribir ficheros en Python
# El uso de ‘x’ hace que si el fichero ya existe se devuelve un error. En el siguiente código creamos un fichero e inmediatamente después intentamos crear un fichero con el mismo nombre con la opción ‘x’. Por lo tanto se devolverá un error.

# In[ ]:


f = open("mi_fichero.txt", "w")
# f = open("mi_fichero.txt", "x")
# Error! Ya existe


# En este otro ejemplo vamos a usar un fichero para establecer una comunicación entre dos funciones. A efectos prácticos puede no resultar muy útil, pero es un buen ejemplo para mostrar la lectura y escritura de ficheros.
# 
# Tenemos por lo tanto una función `escribe_fichero()` que recibe un mensaje y lo escribe en un fichero determinado. Y por otro lado tenemos una función `lee_fichero()` que devuelve el mensaje que está escrito en el fichero.
# 
# Date cuenta lo interesante del ejemplo, ya que podríamos tener estos dos códigos ejecutándose en diferentes maquinas o procesos, y **podrían comunicarse a través del fichero**. Por un lado se escribe y por el otro se lee.

# In[ ]:


# Escribe un mensaje en un fichero
def escribe_fichero(mensaje):
    with open('fichero_comunicacion.txt', 'w') as fichero:
        fichero.write(mensaje)

# Leer el mensaje del fichero        
def lee_fichero():
    mensaje = ""
    with open('fichero_comunicacion.txt', 'r') as fichero:
        mensaje = fichero.read()
    # Borra el contenido del fichero para dejarlo vacío
    f = open('fichero_comunicacion.txt', 'w')
    f.close()
    return mensaje

escribe_fichero("Esto es un mensaje")
print(lee_fichero())


# # Python PEP8: Escribiendo Código Fácil de Leer
# 
# # Introducción
# La PEP8 es una guía que indica las **convenciones estilísticas** a seguir para escribir código Python. Se trata de un conjunto de recomendaciones cuyo objetivo es ayudar a escribir código más legible y abarca desde cómo nombrar variables, al número máximo de caracteres que una línea debe tener.
# 
# De acuerdo con Guido van Rossum, **el código es leído más veces que escrito**, por lo que resulta importante escribir código que no sólo funcione correctamente, sino que además pueda ser leído con facilidad. Esto es precisamente lo que veremos en este artículo.
# 
# Code is read much more often than it is written, __Guido van Rossum__
# 
# Dos mismos códigos pueden realizar lo mismo funcionalmente, pero si no se siguen unas directrices estilísticas, se puede acabar teniendo un código muy difícil de leer. Los problemas más frecuentes suelen ser:
# 
# - Líneas demasiado largas.
# - Nombres de variables poco explicativos.
# - Código mal comentado.
# - Uso incorrecto de espacios y líneas en blanco.
# - Código mal identado.
#   
# Aunque es cierto que ciertas directrices pueden resultar arbitrarias, Python define en la PEP8 las normas estilísticas a seguir para cualquier código parte de la librería estándar, por lo que queda al criterio de cada uno usar estas recomendaciones o no. Sin embargo, prácticamente cualquier código o librería usado por gran cantidad de personas, emplea estas recomendaciones, al haber un amplio consenso en la comunidad.
# 
# # Formatear Código Python PEP8: Linters y Autoformatters
# A veces puede resultar complicado acordarnos de todas y cada una de las normas de la PEP8, por lo que hay herramientas que nos ayudan a corregir automáticamente o indicarnos donde hay problemas en nuestro código. Hay dos tipos de herramientas:
# 
# - Los **linters** como flake8 o pycodestyle.
# - Y los **autoformatters** como black y autopep8.
# 
# Los `autoformatters` se limitan a indicarnos donde nuestro código no cumple con las normas, y en ciertos casos realiza las correcciones automáticamente. Por ejemplo, podemos instalar autopep8 y se puede instalar de la siguiente manera:

# In[ ]:


pip install autopep8


# Y si lo usamos sobre un `script.py` intentará corregir los problemas.

# In[ ]:


autopep8 script.py -v -i


# Veamos un ejemplo. Para alguien recién iniciado en Python, tal vez el siguiente código parezca válido, sin embargo alguien que conozca la PEP8 podrá identificar varios problemas.

# In[ ]:


# script.py
def MiFuncionSuma(A, B, C, imprime = True):
    resultado=A+B+C
    if imprime != False:
        print(resultado)
    return resultado
a          = 4
variable_b = 5
var_c      = 10

MiFuncionSuma(a, variable_b, var_c)


# Usando el comando anterior, se nos informará de todas las reglas que nuestro código no cumple, para que las podamos corregir. Es importante notar que existen reglas que pueden ser corregidas automáticamente, y otras que no.
# 
# - Todo lo relativo al uso de espacios o líneas en blanco, puede ser corregido automáticamente por autopep8.
# - Sin embargo autopep8 nunca modificará el nombre de una variable, por lo que si incumplimos alguna norma en lo relativo a nombrar variables deberemos corregir de forma manual las ocurrencias.
#   
# El código anterior incumple las siguientes reglas:
# 
# - E251: Uso incorrecto de espacios en imprime = True, debería ser imprime=True.
# - E225: Los operadores como el + deben usar espacios, A + B + C.
# - E712: Usar if imprime en vez de if imprime != False.
# - E305: Después de la declaración de una función debemos dejar dos espacios en blanco.
# - E221: No debemos usar tantos espacios al usar el operador = creando variables.
# - También tenemos otros problemas relacionados con cómo nombrar a funciones y variables. Las funciones y variables deben ir en snake case. Lo veremos en detalle más adelante.
#   
# Teniendo en cuenta lo mencionado, podemos implementar las correcciones para tener un código que cumple con la PEP8.

# In[ ]:


# script.py
def mi_funcion_suma(a, b, c, imprime=True):
    resultado = a + b + a
    if imprime:
        print(resultado)
    return resultado


a = 4
variable_b = 5
var_c = 10

mi_funcion_suma(a, variable_b, var_c)


# Visto ya un ejemplo concreto, a continuación veremos las normas más importantes introducidas en la PEP8.

# # Organización del código
# # Líneas en Blanco
# El uso de líneas en blanco mejora notablemente la legibilidad. Mucho código seguido puede ser difícil de leer, pero un uso excesivo de líneas en blanco puede ser molesto. Python deja su uso a nuestro criterio, siempre y cuando cumplamos lo siguiente:
# 
# - Rodear las funciones y clases con dos líneas en blanco. Cada vez que definamos una clase o una función es necesario dejar dos líneas en blanco por arriba y dos por abajo.
# - Dejar una línea en blanco entre los métodos de una clase. Los métodos de una clase deberán tener una línea en blanco entre ellos.
# - Usar líneas en blanco para agrupar pasos similares. Si tenemos un conjunto de código que realiza una función concreta, es conveniente delimitarlo con una línea en blanco, de la misma manera que un libro separa ideas en párrafos.

# In[ ]:


# 1 espacio entre métodos
# 2 espacios entre clases y funciones
class ClaseA:
    def metodo_a(self):
        pass

    def metodo_b(self):
        pass


class ClaseB:
    def metodo_a(self):
        pass

    def metodo_b(self):
        pass


def funcion():
    pass


# También resulta conveniente separar con una línea diferentes funcionalidades. La siguiente función calcula la media y la mediana, por lo que las separamos con una línea en blanco.

# In[ ]:


def calcula_media_mediana(valores):
    # Calculamos la media
    suma_valores = 0
    for valor in valores:
        suma_valores += valor
    media = suma_valores / len(valores)
    
    # Calculamos la mediana
    valores_ordenados = sorted(valores)
    indice = len(valores) // 2
    if len(valores) % 2:
        mediana = valores_ordenados[indice]
    else:
        mediana = (valores_ordenados[indice]
                   + valores_ordenados[indice + 1]) / 2

    return media, mediana


# # Espacios en Blanco
# El uso de espacios en blanco puede resultar clave para mejorar la legibilidad de nuestro código, y es por lo que la PEP8 nos dice **dónde debemos usar espacios y dónde no**. Se trata de buscar un punto de equilibrio entre un código demasiado disperso y con gran cantidad de espacios, y un código demasiado junto donde no se identifican sus partes.
# 
# Se nos recomienda **usar espacio** con operadores de asignación.

# In[ ]:


# Correcto
x = 5

# Incorrecto
x=5


# Y también con operadores relacionales.

# In[ ]:


# Correcto
if x == 5:
    pass

# Incorrecto
if x==5:
    pass


# Pero cuando tengamos funciones con argumentos por defecto, no debemos dejar espacios.

# In[ ]:


# Correcto
def mi_funcion(parameto_por_defecto=5):
    print(parameto_por_defecto)

# Incorrecto
def mi_funcion(parameto_por_defecto = 5):
    print(parameto_por_defecto)


# Por otro lado se recomienda **no dejar espacios dentro del paréntesis**.

# In[ ]:


def duplica(a):
    return a * 2

# Correcto
duplica(2)

# Incorrecto
duplica( 2 )


# Y tampoco entre **corchetes**.

# In[ ]:


# Correcto
lista = [1, 2, 3]

# Incorrecto
my_list = [ 1, 2, 3, ]


# El uso de los espacios resulta muy útil cuando se combinan varios operadores utilizando diferentes variables, utilizando los espacios para agrupar por orden de mayor prioridad. Es por ello por lo que no dejamos espacios en x**2 ni (x-y) dado que la potencia y el uso de paréntesis son los operadores con mayor prioridad.

# In[ ]:


# Correcto
y = x**2 + 1
z = (x-y) * (x+y)

# Incorrecto
y = x ** 2 + 5
z = (x - y) * (x + y)


# Siguiendo la misma filosofía de agrupar por orden de ejecución, tenemos los siguiente ejemplos, siendo el primero el preferido por algunos linters.

# In[ ]:


# Correcto
if x > 0 and x % 2 == 0:
    print('...')

# Correcto
if x>0 and x%2==0:
    print('...')

# Incorrecto
if x% 2 == 0:
    print('...')


# No usar espacio antes de , en llamadas a funciones o métodos.

# In[ ]:


# Correcto
print(x, y)

# Incorrecto
print(x , y)


# Cuando usemos listas no usar espacios antes del índice o entre el índice y los [].

# In[ ]:


# Correcto
lista[0]

# Incorrecto
lista [1]

# Incorrecto
lista [ 1 ]


# Tampoco usando diccionarios.

# In[ ]:


# Correcto
diccionario['key'] = lista[indice]

# Incorrecto
diccionario ['key'] = lista [indice]


# Por último y aunque pueda parecer raro para la gente que venga de otros lenguajes de programación, no se recomienda alinear las variables como se muestra a continuación.

# In[ ]:


# Correcto
var_a = 0
variable_b = 10
otra_variable_c = 3

# Incorrecto
var_a           = 0
variable_b      = 10
otra_variable_c = 3


# Identación del código
# Como ya hemos visto en otros artículos, Python no usa {} para designar bloques de código como otros lenguajes de programación, sino que usa bloques identados para indicar que un determinado bloque de código pertenece a por ejemplo un if.

# In[ ]:


if x > 5:
    pass


# Un bloque identado **se representa usando cuatro espacios** y aunque el uso del tabulador pueda parecer lo mismo, Python 3 no recomienda su uso. Como regla de oro:
# 
# - Usa siempre cuatro espacios.
# - Usa tabuladores si trabajas sobre código ajeno que ya use tabuladores.
# - Bajo ningún concepto mezcles uso de espacios y tabuladores.
#   
# Por otro lado, también se puede identar el código para evitar tener líneas muy largas, que resultan difíciles de leer. Es importante recordar que la PEP8 limita el tamaño de línea a 79 caracteres.

# In[ ]:


# Correcto
def mi_funcion(primer_parametro, segundo_parametro,
               tercer_parametro, cuarto_parametro,
               quinto_parametro):
    print("Python")

# Incorrecto
def mi_funcion(primer_parametro, segundo_parametro, tercer_parametro, cuarto_parametro, quinto_parametro):
    print("Python")


# Lo siguiente sería incorrecto ya que no se diferencian los argumentos de entrada del bloque de código a ejecutar por la función.

# In[ ]:


# Incorrecto
def mi_funcion(primer_parametro, segundo_parametro,
    tercer_parametro, cuarto_parametro,
    quinto_parametro):
    print("Python")


# Análogamente se puede romper un if en diferentes líneas, útil cuando se usan gran cantidad de condiciones que no entran una una línea.

# In[ ]:


# Correcto
if (condicion_a and
        condicion_b):
    print("Python")


# ## Tamaño de linea
# Se recomienda limitar el tamaño de cada línea a **79 caracteres**, para evitar tener que hacer scroll a la derecha. Este límite también permite tener abiertos múltiples ficheros en la misma pantalla, uno al lado de otro. Por otro lado se limita el uso de docstrings y comentarios a **72 caracteres**.
# 
# En los casos que tengamos una línea que no sea posible romper, podemos usar \ para continuar con la línea en una nueva. Esto es algo que a veces puede darse en los context managers.

# In[ ]:


# Correcto
with open('/esta/ruta/es/muy/pero/que/muy/larga/y/no/entra/en/una/sola/linea/') as fichero_1, \
     open('/esta/ruta/es/muy/pero/que/muy/larga/y/no/entra/en/una/sola/linea/', 'w') as fichero_2:
    fichero_2.write(fichero_1.read())


# # Operaciones largas
# Si queremos realizar una operación muy larga que no entra en una línea, tendremos que dividirla en múltiples. Lo recomendado es usar el operador al principio de cada línea, ya que resulta mas fácil de leer.

# In[ ]:


# Recomendado
income = (variable_a
          + variable_b
          + (variable_c - variable_d)
          - variable_e
          - variable_f)


# # Codificación de ficheros
# Los ficheros se codifican por defecto en ASCII para Python 2 y UTF-8 para Python 3, por lo que será necesario definir la codificación que usemos cuando queramos usar otro tipo.
# 
# Esto resulta muy importante, ya que si queremos almacenar una cadena que contiene caracteres no UTF-8 como ó y ñ, deberemos especificar el tipo de encoding de acuerdo a la PEP263. El siguiente código puede dar problemas.

# In[ ]:


print("La acentuación del Español")
# SyntaxError: Non-UTF-8 code starting with '\xf3' in file script.py on line 1, but no encoding declared; see http://python.org/dev/peps/pep-0263/ for details


# Sin embargo, con un pequeño cambio, podemos cambiar la forma en la que se codifica el texto.

# In[ ]:


# -*- coding: latin-1 -*-
print("La acentuación del Español")
# La acentuación del Español


# Por otro lado, si tienes intención de desarrollar código para la librería estándar de Python, o contribuir en un proyecto con alcance global, debes saber lo siguiente:
# 
# - Todos los identificadores (como variables) deben usar ASCII.
# - También deberán usar Inglés en la medida de lo posible, salvo abreviaciones.
# - Las únicas excepciones son los test para código no ASCII y los nombres de autores.
# 
# # Convenciones al Nombrar Elementos: CamelCase y snake_case
# 
# A la hora de escribir código, todo tiene nombres: variables, clases, funciones, paquetes, módulos, etc. Es por lo tanto muy importante seguir unas directrices determinadas para que nuestro código sea lo más legible posible. No se nombra igual a una clase que a una función, y tampoco suele ser recomendable usar nombres como a o x ya que aporta poca información. A continuación lo vemos en detalle.
# 
# # Eligiendo Nombres
# Antes de nada debemos debemos pensar el nombre que le vamos dar a nuestra variable clase o función. Es importante tener en cuenta lo siguiente:
# 
# - Evitar usar palabras reservadas. Si es necesario usar una palabra reservada como class, usar class_ como alternativa.
# - Evitar usar l O y I, ya que pueden ser confundidas.
# - Usar _variable para especificar uso interno. Por ejemplo from m import * no importaría lo que empieza con _.
# - Se puede usar __variable para invocar el name mangling y hacer privadas determinadas variables o métodos.
# - Para métodos mágicos usar siempre __init__, pero no son nombres que debemos crear sino reutilizar los que Python nos ofrece.
#   
# # Estilos: Camel Case y snake_case
# Supongamos que ya sabemos como vamos a nombrar a nuestra clase, función o variable. Pongamos que queremos llamar a nuestra función “mi función de prueba”. Dado que no podemos utilizar espacios para nombrar variables, hay diferentes alternativas:
# 
# - `mi_funcion_de_prueba`
# - `MiFuncionDePrueba`
# - `MIFUNCIONDEPRUEBA`
# - `MI_FUNCION_DE_PRUEBA`
# - `mifunciondeprueba`
# 
# Algunas de estas alternativas son conocidas como Camel Case o snake_case en el mundo de la programación. Pues bien, Python define cómo nombrar a cada tipo de la siguiente manera:
# 
# - **Funciones**: Letras en minúscula separadas por barra baja: funcion, mi_funcion_de_prueba.
# - **Variables**: Al igual que las funciones: variable, mi_variable.
# - **Clases**: Uso de CamelCase, usando mayúscula y sin barra baja: MiClase, ClaseDePrueba.
# - **Métodos**: Al igual que las funciones, usar snake case: metodo, mi_metodo.
# - **Constantes**: Nombrarlas usando mayúsculas y separadas por barra bajas: UNA_CONSTANTE, OTRA_CONSTANTE.
# - **Módulos**: Igual que las funciones: modulo.py, mi_modulo.py.
# - **Paquetes**: En minúsculas pero sin separar por barra bajas: packete, mipaquete
#   
# En el siguiente fragmento podemos ver su uso.

# In[ ]:


# mi_script.py
CONSTANTE_GLOBAL = 10

class MiClase():
    def mi_primer_metodo(self, variable_a, variable_b):
        return (variable_a + variable_b) / CONSTANTE_GLOBAL


mi_objeto = MiClase()
print(mi_objeto.mi_primer_metodo(5, 5))


# # Importando Paquetes: Orden y Organización
# Los `import` deben separarse en diferentes líneas.

# In[ ]:


# Correcto
import os
import sys


# In[ ]:


# Incorrecto
import os, sys


# Sin embargo cuando se importen varios elementos de una misma librería, si sería correcto importarlos en la misma línea.

# In[ ]:


# Correcto
from subprocess import Popen, PIPE


# Con respecto a su **ubicación**, deberán seguir la siguiente:
# 
# - Deben ir al principio del fichero.
# - Después de comentarios del módulo y docstrings.
# - Antes de los global y las constantes.
#   
# Con respecto a su **organización**, debiendo haber una línea de separación entre cada grupo:
# 
# - Primero las librerías **estándar**.
# - Segundo las librerías **externas**.
# - Tercero las librerías **locales**.
# 
# Con respecto a su **tipo**:
# 
# - Se recomienda usar `imports` **absolutos**.
# - Aunque también se permiten los **relativos**.
#   
# Por último, deben evitarse el `from <módulo> import *`. El uso de `*` importa todo lo presente en el `<módulo>`, por lo que no queda claro que se está usando y que no.

# In[ ]:


# Incorrecto
from collections import *


# Si por ejemplo usamos únicamente `deque` y `defaultdict`, indicarlo.

# In[ ]:


# Correcto
from collections import deque, defaultdict


# # Comas al Final de Línea
# El uso de comas al final de la línea suele ser opcional, salvo cuando se quiera crear tuplas de un sólo elemento como se muestra a continuación.

# In[ ]:


# Correcto
tupla = (1,)
print(tupla[0])
# Salida: 1


# Sin embargo aunque su uso sea opcional en el resto de casos, en ciertas ocasiones puede estar justificado si por ejemplo tenemos una lista de elementos que puede cambiar con el tiempo. En este caso el uso de , al final puede ser de ayuda al sistema de control de versiones que utilicemos (como Git).

# In[ ]:


# Correcto
FICHEROS = [
    'fichero1.txt',
    'fichero2.txt',
]

# Incorrecto
FICHEROS = ['fichero1.txt', 'fichero2.txt',]


# # Comentarios
# Los comentarios son muy importantes para realizar anotaciones a futuros lectores de nuestro código, y aunque resulta difícil definir cómo se se debe comentar el código, hay ciertas directrices que debemos seguir:
# 
# - Cualquier comentario que contradiga el código es peor que ningún comentario. Por ello es muy importante que si actualizamos el código, no olvidarnos de actualizar los comentarios para evitar crear inconsistencias.
# - Los comentarios deben ser frases completas, con la primera letra en mayúsculas.
# - Si el comentario es corto, no hace falta usar el punto y final.
# - Si el código es comentado en Inglés, usar Strunk/White.
# - Aunque cada uno es libre de escribir sus comentarios en el idioma que considere oportuno, se recomienda hacerlo en Inglés.
# - Evitar comentarios poco descriptivos que no aporten nada más allá de lo que ya se ve a simple vista.
# - En lo relativo a los comentarios docstrings, usar la PEP257 como referencia.
#   
# A modo de ejemplo, como hemos explicado es conveniente evitar comentarios redundantes.

# In[ ]:


# Incorrecto
x = x + 1      # Suma 1 a la variable x

# Correcto
x = x + 1      # Compensa el offset producido por la medida


# # Testing en Python
# Dentro de la ingeniería software y la programación en general, el testing es una de las partes más importantes que nos encontraremos en casi cualquier proyecto. De hecho es común dedicar más tiempo a probar que el código funciona correctamente que a escribirlo. A continuación veremos las formas más comunes de testear el código en Python, desde lo más básico a conceptos algo más avanzados.
# 
# ## Tests Manuales y Tests Automatizados
# Aunque sea la primera vez que leas acerca de testing en Python, estoy seguro de que ya has ejecutado tests sobre tu código sin darte cuenta. De acuerdo a su **forma de ejecución**, los podemos clasificar en:
# 
# - Tests **manuales**: Son tests ejecutados manualmente por una persona, probando diferentes combinaciones y viendo que el comportamiento del código es el esperado. Sin duda los has realizado alguna vez.
# - Tests **automáticos**: Se trata de **código que testea que otro código se comporta correctamente**. La ejecución es automática, y permite ejecutar gran cantidad de verificaciones en muy poco tiempo. Es la forma más común, pero no siempre es posible automatizar todo.
#   
# Imaginemos que hemos escrito una función que calcula la media de los valores que se pasan en una lista como entrada.

# In[ ]:


def calcula_media(*args):
    return(sum(*args)/len(*args))


# A nadie se le ocurriría publicar nuestra función `calcula_media` sin haber hecho alguna verificación anteriormente. Podemos por ejemplo probar con los siguientes datos y ver si la función hace lo que se espera de ella. Al hacer esto ya estaríamos probando **manualmente** nuestro código.

# In[ ]:


print(calcula_media([3, 7, 5]))
# 5.0

print(calcula_media([30, 0]))
# 15.0


# Con bases de código pequeñas y donde sólo trabajemos nosotros, tal vez sea suficiente, pero a medida que el proyecto crece puede no ser suficiente. ¿Qué pasa si alguien modifica nuestra función y se olvida de testear que funciona correctamente? Nuestra función habría dejado de funcionar y nadie se habría enterado.
# 
# Es aquí donde los test **automáticos** nos pueden ayudar. Python nos ofrece herramientas que nos permiten escribir tests que son ejecutados automáticamente, y que si fallan darán un error, alertando al programador de que ha “roto” algo. Podemos hacer esto con assert, donde identificamos dos partes claramente:
# 
# - Por un lado tenemos la **llamada a la función** que queremos testear, que devuelve un resultado.
# - Por otro lado tenemos el **resultado esperado**, que comparamos con el resultado devuelto por la función. Si no es igual, se lanza un error.

# In[ ]:


assert(calcula_media([3, 7, 5]) == 5.0)
assert(calcula_media([30, 0]) == 15.0)


# Nótese que los valores de 5 y 15 los hemos calculado manualmente, y corresponden con la media de 3,7,5 y 30,0 respectivamente. Si por cualquier motivo alguien rompe nuestra función `calcula_media()`, cuando los tests se ejecuten lanzaran una excepción.

# In[ ]:


Traceback (most recent call last):
  File "ejemplo.py", line 7, in <module>
    assert((calcula_media([30, 0]) == 15.0))
AssertionError


# En proyectos grandes, es común que antes de permitirnos hacer merge de nuestro código en master, se nos obligue a ejecutar un conjunto de tests automatizados. Si todos pasan, se asumirá que nuestro código funciona y que no hemos “roto” nada, por lo que tendremos el visto bueno.
# 
# Visto esto, tal vez pueda parecer que los test automatizados son lo mejor, sin embargo **no siempre se pueden automatizar los tests**. Si por ejemplo estamos trabajando con interfaces de usuario, es posible que no podamos automatizarlos, ya que se sigue necesitando a un humano que verifique los cambios visualmente.
# 
# ## Tests Unitarios en Python con unittest
# Aunque el uso de `assert()` puede ser suficiente para nuestros tests, a veces se nos queda corto y necesitamos librerías como unittest, que ofrecen alguna que otra funcionalidad que nos hará la vida más fácil. Veamos un ejemplo. Recordemos nuestra función `calcula_media`, que es la que queremos testear.

# In[ ]:


# funciones.py
def calcula_media(*args):
    return(sum(*args)/len(*args))


# Podemos usar `unittest` para crear varios tests que verifiquen que nuestra función funciona correctamente. Aunque la estructura de un conjunto de tests se puede complicar más, la estructura será siempre muy similar a la siguiente:
# 
# - Creamos una clase `Test<NombreDeLoQueSePrueba>` que hereda de `unittest.TestCase`.
# - Definimos varios tests como métodos de la clase, usando `test_<NombreDelTest>` para nombrarlos.
# - En cada test ejecutamos las comprobaciones necesarias, usando `assertEqual` en vez de `assert`, pero su comportamiento es totalmente análogo.

# In[ ]:


# tests.py
from funciones import calcula_media
import unittest

class TestCalculaMedia(unittest.TestCase):
    def test_1(self):
        resultado = calcula_media([10, 10, 10])
        self.assertEqual(resultado, 10)

    def test_2(self):
        resultado = calcula_media([5, 3, 4])
        self.assertEqual(resultado, 4)

if __name__ == '__main__':
    unittest.main()


# Si ejecutamos el código anterior, obtendremos el siguiente resultado. Esta es una de las ventajas de `unittest`, ya que nos muestra información sobre los tests ejecutados, el tiempo que ha tardado y los resultados.

# In[ ]:


Ran 2 tests in 0.006s

OK


# Por otro lado, usando -v podemos obtener más información sobre cada test ejecutado con su resultado individualmente. Si tenemos gran cantidad de tests suele ser recomendable usarla, ya que será más fácil localizar los tests que han fallado.

# In[ ]:


$ python -m unittest -v tests

test_1 (tests.TestCalculaMedia) ... ok
test_2 (tests.TestCalculaMedia) ... ok

----------------------------------------------------------------------
Ran 2 tests in 0.000s

OK


# Por último, si tenemos varios ficheros de test, podemos usar `discover`, para decirle a Python que busque en la carpeta todos los tests y los ejecute.

# In[ ]:


$ python -m unittest discover -v


# # Otras comprobaciones en unittest
# Anteriormente hemos visto el uso de `.assertEqual(a, b)` que simplemente verifica que dos valores `a` y `b` son iguales, y de lo contrario da error. Sin embargo `unittest` nos ofrece un amplio abanico de opciones. Nótese que existen algunas variaciones usando “not”, como `assertNotIn()`:
# 
# - `.assertEqual(a, b)`: Verifica la igualdad de ambos valores.
# - `.assertTrue(x)`: Verifica que el valor es `True`.
# - `.assertFalse(x)`: Verifica que el valor es `False`.
# - `.assertIs(a, b)`: Verifica que ambas variables son la misma (ver operador is).
# - `.assertIsNone(x)`: Verifica que el valor es `None`.
# - `.assertIn(a, b)`: Verifica que `a` pertenece al iterable `b` (ver operador in).
# - `.assertIsInstance(a, b)`: Verifica que a es una instancia de `b`
# - `.assertRaises(x)`: Verifica que se lanza una excepción.

# In[ ]:


import unittest
class TestEjemplos(unittest.TestCase):
    def test_in(self):
    	# Ok ya que 1 esta contenido en [1, 2, 3]
        self.assertIn(1, [1, 2, 3])

    def test_is(self):
        a = [1, 2, 3]
        b = a
        # Ok ya que son el mismo objeto
        self.assertIs(a, b)

    def test_excepcion(self):
    	# Dividir 0/0 da error, pero es lo esperado por el test
        with self.assertRaises(ZeroDivisionError):
            x = 0/0


# In[ ]:


$ python -m unittest -v tests

test_excepcion (tests.TestEjemplos) ... ok
test_in (tests.TestEjemplos) ... ok
test_is (tests.TestEjemplos) ... ok

----------------------------------------------------------------------
Ran 3 tests in 0.000s

OK


# # Usando setUp y tearDown
# Otra de las ventajas de usar `unittest`, es que nos ofrece la posibilidad de definir funciones comunes que son ejecutadas antes y después de cada test. Estos métodos son `setUp()` y `tearDown()`.

# In[ ]:


import unittest
class TestEjemplos(unittest.TestCase):
    def setUp(self):
        print("Entra setUp")
    def tearDown(self):
        print("Entra tearDown")

    def test_1(self):
        print("Test: test_1")
    def test_2(self):
        print("Test: test_2")


# Siendo el resultado el siguiente. Podemos ver que hace una especie de sandwich con cada test, metiéndolo entre `setUp` y `tearDown`. Nótese que si ambas funciones realizan siempre lo mismo, tal vez se pueda usar un `TestSuite` con una función común para todos los tests, pero se trata de un concepto algo más avanzado que dejaremos para otro artículo.

# In[ ]:


$ python -m unittest -v tests

test_1 (tests.TestEjemplos) ... Entra setUp
Test: test_1
Entra tearDown
ok
test_2 (tests.TestEjemplos) ... Entra setUp
Test: test_2
Entra tearDown
ok

----------------------------------------------------------------------
Ran 2 tests in 0.000s

OK


# # Evitando Side Effects
# Hasta ahora hemos visto las herramientas que necesitamos para escribir nuestros tests, pero es también muy importante seguir una serie de buenas practicas a la hora de escribir nuestro código. Uno de los principios más importantes a seguir es el Principio de Responsabilidad Única o SRP, que nos dice que el código (bien sea una clase o una función) debe tener una única responsabilidad. Si hace demasiadas cosas, será más complicado de modificar y mantener, y además será más complicado de testear.
# 
# Por lo tanto es tan importante escribir buenos tests que sean completos y tengan en cuenta todas las posibles casuísticas como escribir código que pueda ser testeado de manera fácil.
