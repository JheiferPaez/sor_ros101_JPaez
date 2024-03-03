Zero to ROS

#Guia de git
https://www.youtube.com/watch?v=N8ynbLL7acE

#Por primera vez
echo "# sor_ros101_jpaez" >> README.md
git init
git add README.md
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/JheiferPaez/sor_ros101_jpaez.git
git push -u origin main


#Para subir un solo archivo
git add .
git commit -m "Añadì el README.md y lo modifiqué"
git push -u origin main

#Añadir otra rama
git branch          // Ver las ramas disponibles
git branch rama2    // Crear la nueva rama llamada rama2
git checkout rama2  // Cambio a la nueva rama llamada rama2
git branch          // Ver las ramas disponibles

#Subir cambios a otra rama
git add .
git commit -m "hice modificaciones a los archivs y añadí una nueva rama"
git push -u origin rama2

#Fusionar cambios de ramas
git checkout main   // Regresar a la rama principal
git merge rama2     // Fusionar rama2 a rama main
git commit -m "codigo fusionado"
git push origin main//

#crear rama con versiones 
git branch rama3antigua 95a6e9d85b050dcd5afcd6c2d33a7790becce52b
git checkout rama3antigua




