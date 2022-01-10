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
		1.Clonez le repository en utilisant <mark>git clone</mark><br>
		2.Se déplacer dans le répertoire racine SoftDesk en utilisant la commande <mark>cd softDesk</mark><br>
		3.Créer un environnement virtuel pour le projet avec la commande <mark>python -m venv env</mark><br>
		4.Activez l'environnement virtuel avec la commande <mark>env\Scripts\activate.bat</mark><br>
		5.Installez les dépendances du project avec la commande <mark>pip install -r requirements.txt</mark><br>
	</p>
	<h3>Documentation et détails d'utilisation des endpoints de l'API</h3>
	<p>
		Une fois le serveur lancé, lisez le document  suivant avant de faire vos premières requetes à l'API.<br>
	</p>
	<table>
		<tr>
			<th>Point de terminaison d'API</th>
			<th>Méthode HTTP</th>
			<th>URI</th>
		</tr>
		<tr>
			<td>Inscription de l'utilisateur</td>
			<td>POST</td>
			<td>/sign-up/</td>
		</tr>
		<tr>
			<td>Connexion de l'utilisateur</td>
			<td>POST</td>
			<td>/login/</td>
		</tr>
		<tr>
			<td>Récupérer la liste de tous les projets (projects) rattachés à l'utilisateur (user) connecté</td>
			<td>GET</td>
			<td>/projects/</td>
		</tr>
		<tr>
			<td>Créer un projet</td>
			<td>POST</td>
			<td>/projects/</td>
		</tr>
		<tr>
			<td>Récupérer les détails d'un projet (project) via son id</td>
			<td>GET</td>
			<td>/projects/{id}/</td>
		</tr>
		<tr>
			<td>Mettre à jour un projet</td>
			<td>PUT</td>
			<td>/projects/{id}/</td>
		</tr>
		<tr>
			<td>Supprimer un projet et ses problèmes</td>
			<td>DELETE</td>
			<td>/projects/{id}/</td>
		</tr>
		<tr>
			<td>Ajouter un utilisateur (collaborateur) à un projet</td>
			<td>POST</td>
			<td>/projects/{id}/users/</td>
		</tr>
		<tr>
			<td>Récupérer la liste de tous les utilisateurs (users) attachés à un projet (project)</td>
			<td>GET</td>
			<td>/projects/{id}/users/</td>
		</tr>
		<tr>
			<td>Supprimer un utilisateur d'un</td>
			<td>DELETE</td>
			<td>/projects/{id}/users/{id}</td>
		</tr>
	</table>
</body>
</html>