# film_suggestions

Interactive AI-Based Web Application for Personalized Series Movies and Animations Recommendations

## Εγκατάσταση project dependencies

Στο root directory του project:

  ```console
  pip install -r requirements.txt
  ```

## Εγκατάσταση της εφαρμογής
	
Από το root directory του project:
<br><br>
**Απαιτείται ansible-core==2.13.4**

  ```console
  cd ansible
  ansible-playbook -i hosts.ini deploy.yaml
  ```


## Eκτελεση Python Formatters/Linters

Εκτέλεση formatters/linters *μία φορά*:

  ```console
  ./ops format_code
  ```

Για εκτέλεση formatters/linters σε *watch mode*: <br>
*(κάθε φορά που γίνεται μια αλλαγή στα αρχεία Python, οι formatters/linters θα εκτελούνται)*

  ```console
  ./ops dev
  ```
