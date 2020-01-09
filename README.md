## TDD: desarrollo guiado por pruebas Python
**Desarrollo guiado por pruebas de software, o Test-driven development (TDD)** es una práctica de ingeniería de software que involucra otras dos prácticas: Escribir las pruebas primero (Test First Development) y Refactorización (Refactoring). Para escribir las pruebas generalmente se utilizan las pruebas unitarias (unit test en inglés). En primer lugar, se escribe una prueba y se verifica que las pruebas fallan. A continuación, se implementa el código que hace que la prueba pase satisfactoriamente y seguidamente se refactoriza el código escrito. El propósito del desarrollo guiado por pruebas es lograr un código limpio que funcione. La idea es que los requisitos sean traducidos a pruebas, de este modo, cuando las pruebas pasen se garantizará que el software cumple con los requisitos que se han establecido. (Wikipedia)
A diferencia de programar un proyecto y luego añadir pruebas, la idea del TDD es desarrollar el software a partir de las propias pruebas, dejando que éstas nos guíen durante el proceso.
De esta forma cada funcionalidad ya es concebida desde el principio con la idea de superar un test y por tanto está monitorizada para su correcto funcionamiento en el futuro.
Proceso de desarrollo:  
**Para hacer TDD hay que seguir un orden estricto:**  
1. Escribir una prueba, que recoja los requisitos de la funcionalidad que vamos a implementar.
2. Ejecutar la prueba y comprobar que falla, ya que todavía no habremos implementado la funcionalidad.
3. Implementar la funcionalidad, con el código mínimo necesario.
4. Volver a ejecutar la prueba, que en esta ocasión debería pasar correctamente, y si no es así corregir el código hasta que la pase.
5. Refactorizar el código, borrando redundancias e incongruencias, siempre comprobando que los tests siguen validando bien.
6. Volver a empezar, para implementar el siguiente requisito.

Ejemplo simple (IDE PyCharm)
1.	Creamos nuevo archivo Python Test 
pytest-test.py


