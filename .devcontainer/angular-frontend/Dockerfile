FROM node:20.12.2-bullseye

WORKDIR /workspace

COPY package.json package.json

RUN npm install -g @angular/cli \
    && npm install

COPY . .

# EXPOSE 4200

# CMD ["python", "main.py"]