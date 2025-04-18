# AngularFrontend

- Install Angular CLI version `19.0.6`

```bash
npm install @angular/cli@19.0.6 -g
```

- Create a new project

```bash
ng new app --directory ./ --skip-git
```

- Update `package.json` 

```json
  "scripts": {
    "ng": "ng",
    "start": "ng serve --host 0.0.0.0 --port 4200",
    "build": "ng build",
    "watch": "ng build --watch --configuration development",
    "test": "ng test"
  }
```

