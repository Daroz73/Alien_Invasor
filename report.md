# Informe de Desarrollo Técnico: Alien Invasisor

## 1. Resumen Ejecutivo
Este proyecto consiste en el desarrollo de un motor de juego funcional utilizando el patrón de diseño **Modelo-Vista-Controlador (MVC)** simplificado. Se enfoca en la gestión eficiente de recursos de hardware y la lógica de colisiones en tiempo real.

## 2. Decisiones de Arquitectura

### 2.1. Gestión de Estado (`game_stats.py`)
Se implementó una clase dedicada para centralizar el estado del juego (vidas, puntuación, nivel activo). Esto permite un reinicio limpio de las estadísticas sin necesidad de instanciar de nuevo todo el motor gráfico, optimizando el uso de memoria.

### 2.2. Programación Orientada a Objetos (POO)
El uso de herencia es clave en el proyecto. Por ejemplo, las clases `Ship`, `Alien` y `Bullet` heredan de `pygame.sprite.Sprite`, lo que permite:
- Agrupar entidades en `pygame.sprite.Group`.
- Realizar detecciones de colisiones masivas de forma eficiente mediante `spritecollideany` y `groupcollide`.

### 2.3. Desacoplamiento de Configuraciones (`setting.py`)
Se extrajeron todas las constantes (velocidades, colores, dimensiones) a una clase `Setting`. Esto facilita el equilibrado del juego (*game balancing*) sin necesidad de modificar la lógica central del código.

## 3. Desafíos Técnicos Resueltos

- **Escalabilidad de Dificultad:** Se diseñó un método `initialize_dynamic_settings` que utiliza factores multiplicadores (`speed_up_scale`) para aumentar la agilidad del juego de manera exponencial pero controlada.
- **Renderizado de UI:** La clase `Scoreboard` gestiona la conversión de datos numéricos a imágenes renderizadas en tiempo real, asegurando que la información de usuario siempre esté actualizada en pantalla sin caídas de FPS.

## 4. Optimización de Rendimiento
- **Gestión de Proyectiles:** Se implementó una limpieza automática de balas que salen de los límites de la pantalla para evitar fugas de memoria y procesamientos innecesarios en el grupo de sprites.
- **Transformaciones:** Se utilizó `pygame.transform.scale` durante la inicialización de los objetos para asegurar que el escalado de imágenes no ocurra dentro del bucle principal del juego.

## 5. Conclusión
El proyecto demuestra una base sólida en el desarrollo de software con Python, aplicando buenas prácticas de organización de archivos, gestión de eventos y lógica matemática aplicada a coordenadas 2D.