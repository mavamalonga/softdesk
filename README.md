<<!DOCTYPE html>
<html>
<head>
</head>
<body>
	<h1>SoftDesk-API</h1>
	<p>
		SoftDesk, une société d'édition de logiciels de développement et de collaboration, a décidé de publier une application permettant de remonter et suivre des problèmes techniques (issue tracking system). Cette solution s’adresse à des entreprises clientes, en B2B
	</p>
	<h2>Installtion</h2>
	<p>
		1.Clonez le repository en utilisant <mark>git clone</mark>
		2.Se déplacer dans le répertoire racine SoftDesk en utilisant la commande <mark>cd softDesk</mark>
		3.Créer un environnement virtuel pour le projet avec la commande <mark>python -m venv env</mark>
		4.Activez l'environnement virtuel avec la commande <mark>env\Scripts\activate.bat</mark>
		5.Installez les dépendances du project avec la commande <mark>pip install -r requirements.txt</mark>
	</p>
	<h3>Documentation et détails d'utilisation des endpoints de l'API</h3>
	<p>
		Une fois le serveur lancé, lisez le document  suivant avant de faire vos premières requetes à l'API.<br><br>

		Point de terminaison d'API

		Méthode HTTP
		URI
		Inscription de l'utilisateur
		POST
		/signup/
		Connexion de l'utilisateur
		POST
		/login/
		Récupérer la liste de tous les projets (projects) rattachés à l'utilisateur (user) connecté
		GET
		/projects/
		Créer un projet
		POST
		/projects/
		Récupérer les détails d'un projet (project) via son id
		GET
		/projects/{id}/
		Mettre à jour un projet
		PUT
		/projects/{id}/
		Supprimer un projet et ses problèmes
		DELETE
		/projects/{id}/
		Ajouter un utilisateur (collaborateur) à un projet
		POST
		/projects/{id}/users/
		Récupérer la liste de tous les utilisateurs (users) attachés à un projet (project)
		GET
		/projects/{id}/users/
		Supprimer un utilisateur d'un projet
		DELETE
		/projects/{id}/users/{id}
		Récupérer la liste des problèmes (issues) liés à un projet (project)
		GET
		/projects/{id}/issues/
		Créer un problème dans un projet
		POST
		/projects/{id}/issues/
		Mettre à jour un problème dans un projet
		PUT
		/projects/{id}/issues/{id}
		Supprimer un problème d'un projet
		DELETE
		/projects/{id}/issues/{id}
		Créer des commentaires sur un problème
		POST
		/projects/{id}/issues/{id}/comments/
		Récupérer la liste de tous les commentaires liés à un problème (issue)
		GET
		/projects/{id}/issues/{id}/comments/
		Modifier un commentaire
		PUT
		/projects/{id}/issues/{id}/comments/{id}
		Supprimer un commentaire
		DELETE
		/projects/{id}/issues/{id}/comments/{id}
		Récupérer un commentaire (comment) via son id
		GET
		/projects/{id}/issues/{id}/comments/{id}

	</p> 
</body>
</html>