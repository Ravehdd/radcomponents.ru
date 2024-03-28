# Используем Node.js как основу для сборки фронтенда
FROM node:latest

WORKDIR /app

# Копируем package.json и package-lock.json
COPY package*.json ./

# Устанавливаем зависимости


# Копируем все файлы фронтенда
COPY . .
RUN chmod +x /app/node_modules/.bin/react-scripts
RUN npm install

# Собираем фронтенд приложение
CMD npm start