<p align="center">
    <img src="https://raw.githubusercontent.com/PKief/vscode-material-icon-theme/ec559a9f6bfd399b82bb44393651661b08aaf7ba/icons/folder-markdown-open.svg" align="center" width="30%">
</p>
<p align="center"><h1 align="center">DEMENTIA-ASSISTANT</h1></p>
<p align="center">
	<em>Empowering Memories, Enhancing Lives with Technology.</em>
</p>
<p align="center">
	<img src="https://img.shields.io/github/license/eloicito333/dementia-assistant?style=default&logo=opensourceinitiative&logoColor=white&color=0080ff" alt="license">
	<img src="https://img.shields.io/github/last-commit/eloicito333/dementia-assistant?style=default&logo=git&logoColor=white&color=0080ff" alt="last-commit">
	<img src="https://img.shields.io/github/languages/top/eloicito333/dementia-assistant?style=default&color=0080ff" alt="repo-top-language">
	<img src="https://img.shields.io/github/languages/count/eloicito333/dementia-assistant?style=default&color=0080ff" alt="repo-language-count">
</p>
<p align="center"><!-- default option, no dependency badges. -->
</p>
<p align="center">
	<!-- default option, no dependency badges. -->
</p>
<br>

## 🔗 Table of Contents

- [📍 Overview](#-overview)
- [👾 Features](#-features)
- [📁 Project Structure](#-project-structure)
  - [📂 Project Index](#-project-index)
- [🚀 Getting Started](#-getting-started)
  - [☑️ Prerequisites](#-prerequisites)
  - [⚙️ Installation](#-installation)
  - [🤖 Usage](#🤖-usage)
  - [🧪 Testing](#🧪-testing)
- [📌 Project Roadmap](#-project-roadmap)
- [🔰 Contributing](#-contributing)
- [🎗 License](#-license)
- [🙌 Acknowledgments](#-acknowledgments)

---

## 📍 Overview

The Dementia Assistant project leverages advanced technology to support individuals with dementia by managing reminders and processing spoken data efficiently. This innovative tool ensures seamless interaction through voice commands and real-time transcription, enhancing daily life management for those affected. It's designed for caregivers, healthcare providers, and families, offering a reliable and user-friendly solution to improve communication and care in dementia management scenarios.

---

## 👾 Features

|      | Feature         | Summary       |
| :--- | :---:           | :---          |
| ⚙️  | **Architecture**  | <ul><li>Utilizes both Python and JavaScript, indicating a likely split between backend (Python) and frontend or utility scripts (JavaScript).</li><li>Structured with separate directories for different servers (HTTP and WebSocket), suggesting a microservices architecture.</li><li>Integration with MongoDB and use of environment variables for configuration, enhancing flexibility and scalability.</li></ul> |
| 🔩 | **Code Quality**  | <ul><li>Presence of `package-lock.json` ensures consistent dependency versions, enhancing reliability.</li><li>Use of configuration files (`config.js`) for setting up environment variables, promoting good practices in configuration management.</li><li>Codebase includes multiple languages and dependency managers, which may pose challenges in maintaining consistency across components.</li></ul> |
| 📄 | **Documentation** | <ul><li>Documentation includes install and usage commands, facilitating easier setup and usage.</li><li>Use of badges in documentation for visual enhancement and quick reference.</li><li>Documentation seems to be split across different technologies (npm for JavaScript, pip for Python), which could require users to be familiar with both ecosystems.</li></ul> |
| 🔌 | **Integrations**  | <ul><li>Integrates with MongoDB for database operations, suitable for handling complex data structures needed in a dementia assistant application.</li><li>Uses npm and pip, indicating integration with Node.js and Python libraries respectively.</li><li>No explicit mention of external APIs or services beyond MongoDB, which might limit external data interaction capabilities.</li></ul> |
| 🧩 | **Modularity**    | <ul><li>Project structure suggests modularity with separate directories and requirements for different components (HTTP server, WebSocket server).</li><li>Modular use of npm and pip could allow for independent updates and maintenance of parts of the project.</li><li>Modularity may aid in isolating issues and scaling specific components of the application as needed.</li></ul> |
| 🧪 | **Testing**       | <ul><li>Includes a command for running tests using pytest, indicating some level of automated testing.</li><li>Lack of detailed testing documentation or test files in the provided details suggests potential areas for improvement in test coverage and documentation.</li><li>Testing appears to be more focused on the Python components.</li></ul> |
| ⚡️  | **Performance**   | <ul><li>Use of MongoDB and efficient handling of HTTP requests likely contribute to good performance in data-intensive operations.</li><li>No explicit mention of performance optimization techniques or metrics.</li><li>Performance may be impacted by the dual-language architecture if not properly managed.</li></ul> |

---

## 📁 Project Structure

```sh
└── dementia-assistant/
    ├── LICENSE
    ├── README.md
    ├── client
    │   ├── .env.demo
    │   ├── .gitignore
    │   ├── client.py
    │   ├── essential_data.py
    │   ├── main.py
    │   ├── player.py
    │   ├── program_settings.py
    │   ├── requirements.txt
    │   ├── stream_constants.py
    │   ├── stream_handler.py
    │   └── utils
    └── servers
        ├── http
        └── websocket
```


### 📂 Project Index
<details open>
	<summary><b><code>DEMENTIA-ASSISTANT/</code></b></summary>
	<details> <!-- __root__ Submodule -->
		<summary><b>__root__</b></summary>
		<blockquote>
			<table>
			</table>
		</blockquote>
	</details>
	<details> <!-- servers Submodule -->
		<summary><b>servers</b></summary>
		<blockquote>
			<details>
				<summary><b>http</b></summary>
				<blockquote>
					<table>
					<tr>
						<td><b><a href='https://github.com/eloicito333/dementia-assistant/blob/master/servers/http/package-lock.json'>package-lock.json</a></b></td>
						<td>- The file `package-lock.json` located in the `servers/http` directory is a crucial component of the `dementia_assistant_http_server` module within the broader project architecture<br>- This file specifically locks down the versions of dependencies used by the HTTP server, ensuring consistent installations across different environments<br>- The server itself is likely responsible for handling HTTP requests, interfacing with a MongoDB database, and managing environmental variables, which is indicated by the dependencies listed (Express for server operations, MongoDB for database interactions, and dotenv for environment configuration)<br>- This setup is essential for the reliable operation of the server component in the dementia assistant application, contributing to the stability and predictability of the server's behavior in production environments.</td>
					</tr>
					<tr>
						<td><b><a href='https://github.com/eloicito333/dementia-assistant/blob/master/servers/http/config.js'>config.js</a></b></td>
						<td>- Configures environment variables and exports essential settings for the HTTP server, including port configuration, authentication parameters, and database connectivity details<br>- It ensures the server operates with the necessary credentials and connections, facilitating secure and efficient interactions with external services and databases within the broader application architecture.</td>
					</tr>
					<tr>
						<td><b><a href='https://github.com/eloicito333/dementia-assistant/blob/master/servers/http/.env.demo'>.env.demo</a></b></td>
						<td>- Establishes environment variables crucial for configuring the HTTP server within the broader application architecture<br>- It specifies settings for API access, database connectivity, authentication, and server port configuration, ensuring secure and efficient operation of server-side functionalities<br>- Essential for initializing and maintaining the application's runtime environment.</td>
					</tr>
					<tr>
						<td><b><a href='https://github.com/eloicito333/dementia-assistant/blob/master/servers/http/index.js'>index.js</a></b></td>
						<td>- Initializes the Dementia Assistant server by creating and configuring an HTTP server using the Express framework<br>- It sets up the server to listen on a port defined in the configuration file, providing feedback upon successful launch<br>- This component is crucial for handling incoming web requests and serving the application's functionalities.</td>
					</tr>
					<tr>
						<td><b><a href='https://github.com/eloicito333/dementia-assistant/blob/master/servers/http/expressServer.js'>expressServer.js</a></b></td>
						<td>- ExpressServer.js establishes the HTTP server framework using Express, integrating middleware for logging and authentication<br>- It configures API routes for spoken data and reminders, organizing them under a base-level router<br>- This setup ensures efficient request handling and response delivery, contributing to the modular architecture of the web application.</td>
					</tr>
					<tr>
						<td><b><a href='https://github.com/eloicito333/dementia-assistant/blob/master/servers/http/package.json'>package.json</a></b></td>
						<td>- Serves as the configuration backbone for the dementia_assistant_http_server, specifying operational parameters for the HTTP server component of the project<br>- It defines dependencies essential for server operation, such as Express for routing and MongoDB for database interactions, and sets up scripts for development and production environments.</td>
					</tr>
					</table>
					<details>
						<summary><b>lib</b></summary>
						<blockquote>
							<table>
							<tr>
								<td><b><a href='https://github.com/eloicito333/dementia-assistant/blob/master/servers/http/lib/mongodb.js'>mongodb.js</a></b></td>
								<td>- Establishes a connection to MongoDB using parameters defined in the project's configuration<br>- It initializes a MongoDB client and connects to the specified database, making the database object available for other parts of the application to perform data operations<br>- This setup is crucial for managing data interactions within the server's architecture.</td>
							</tr>
							<tr>
								<td><b><a href='https://github.com/eloicito333/dementia-assistant/blob/master/servers/http/lib/openai.js'>openai.js</a></b></td>
								<td>- OpenAIHelper, defined within the servers/http/lib/openai.js, facilitates interaction with the OpenAI API by generating text embeddings<br>- It initializes with an API key and provides a method to create embeddings from text, which are essential for processing and analyzing textual data efficiently within the broader application architecture.</td>
							</tr>
							</table>
						</blockquote>
					</details>
					<details>
						<summary><b>routes</b></summary>
						<blockquote>
							<table>
							<tr>
								<td><b><a href='https://github.com/eloicito333/dementia-assistant/blob/master/servers/http/routes/spokenData.js'>spokenData.js</a></b></td>
								<td>- SpokenDataRoutes in the HTTP server module manages spoken data interactions, enabling document storage and retrieval within a MongoDB database<br>- It supports inserting spoken data with optional confidential information and searching through documents based on text, date, or speaker criteria using OpenAI embeddings for enhanced query capabilities.</td>
							</tr>
							<tr>
								<td><b><a href='https://github.com/eloicito333/dementia-assistant/blob/master/servers/http/routes/reminders.js'>reminders.js</a></b></td>
								<td>- Manages CRUD operations for reminders within a MongoDB collection via an Express router<br>- It supports adding, retrieving, updating, and deleting reminder items, ensuring data validation and error handling to maintain data integrity and provide feedback on operation outcomes.</td>
							</tr>
							</table>
						</blockquote>
					</details>
					<details>
						<summary><b>middleware</b></summary>
						<blockquote>
							<table>
							<tr>
								<td><b><a href='https://github.com/eloicito333/dementia-assistant/blob/master/servers/http/middleware/auth.js'>auth.js</a></b></td>
								<td>- AuthMiddleware, located within the HTTP server's middleware directory, serves as a security gatekeeper by verifying incoming requests against a predefined authentication string<br>- It ensures that only requests with valid authorization proceed, otherwise, it denies access by responding with a 401 status code, indicating failed authentication<br>- This component is crucial for enforcing access control across the server's endpoints.</td>
							</tr>
							</table>
						</blockquote>
					</details>
				</blockquote>
			</details>
			<details>
				<summary><b>websocket</b></summary>
				<blockquote>
					<table>
					<tr>
						<td><b><a href='https://github.com/eloicito333/dementia-assistant/blob/master/servers/websocket/reminders_manager.py'>reminders_manager.py</a></b></td>
						<td>- Manages reminders within a websocket server, scheduling and updating notification times based on user-defined frequencies and conditions<br>- Utilizes a threading model to handle reminder operations asynchronously, interfacing with a database through an API helper to retrieve and update reminder data.</td>
					</tr>
					<tr>
						<td><b><a href='https://github.com/eloicito333/dementia-assistant/blob/master/servers/websocket/program_settings.py'>program_settings.py</a></b></td>
						<td>- Manages configuration settings specific to the WebSocket server within the broader application architecture<br>- The settings ensure detailed logging through verbosity and prevent deletion operations, enhancing stability and traceability during WebSocket communications<br>- These configurations play a crucial role in maintaining consistent server behavior and facilitating debugging processes.</td>
					</tr>
					<tr>
						<td><b><a href='https://github.com/eloicito333/dementia-assistant/blob/master/servers/websocket/api_helper.py'>api_helper.py</a></b></td>
						<td>- APIHelper in `servers/websocket/api_helper.py` serves as an interface for interacting with internal APIs, managing spoken data and reminders<br>- It initializes connections, handles CRUD operations for documents and reminders, and ensures secure communication through API keys and headers, streamlining data management within the application's architecture.</td>
					</tr>
					<tr>
						<td><b><a href='https://github.com/eloicito333/dementia-assistant/blob/master/servers/websocket/handler.py'>handler.py</a></b></td>
						<td>- Handler.py manages the processing of potentially confidential information within user messages by identifying and anonymizing sensitive data<br>- It utilizes an AI model to detect confidential content, replaces it with placeholders, and forwards the sanitized data along with metadata for further handling by the system.</td>
					</tr>
					<tr>
						<td><b><a href='https://github.com/eloicito333/dementia-assistant/blob/master/servers/websocket/stream_constants.py'>stream_constants.py</a></b></td>
						<td>- Defines constants critical for managing audio data in the WebSocket server, including frequency ranges for vocal detection, sample rates for stream compatibility with the OpenAI TTS API, and block sizes for audio processing<br>- These constants ensure efficient audio data buffering, transmission, and context preservation during live audio streaming sessions.</td>
					</tr>
					<tr>
						<td><b><a href='https://github.com/eloicito333/dementia-assistant/blob/master/servers/websocket/.env.demo'>.env.demo</a></b></td>
						<td>- Provides a template for setting environment variables crucial for the WebSocket server's operation within the project<br>- It includes placeholders for API keys, internal URLs, authentication tokens, and the server port, ensuring secure and configurable communication channels and service integration essential for the system's functionality and security.</td>
					</tr>
					<tr>
						<td><b><a href='https://github.com/eloicito333/dementia-assistant/blob/master/servers/websocket/main.py'>main.py</a></b></td>
						<td>- Initiates a WebSocket server for a voice assistant, setting up components for user interaction through voice commands<br>- It configures transcription settings, initializes audio playback, and manages voice data processing<br>- The server also handles user preferences for verbosity and data retention, enhancing user experience with personalized greetings and operational modes.</td>
					</tr>
					<tr>
						<td><b><a href='https://github.com/eloicito333/dementia-assistant/blob/master/servers/websocket/openai_client.py'>openai_client.py</a></b></td>
						<td>- Establishes the connection between the server's websocket component and OpenAI's API by initializing the OpenAI client using environment-specific configurations<br>- This setup enables the application to interact dynamically with OpenAI services, facilitating real-time data processing and response generation within the broader system architecture.</td>
					</tr>
					<tr>
						<td><b><a href='https://github.com/eloicito333/dementia-assistant/blob/master/servers/websocket/server.py'>server.py</a></b></td>
						<td>- SocketServer in `servers/websocket/server.py` establishes a WebSocket server using Flask and Socket.IO to manage real-time, bi-directional communication with clients<br>- It handles client connections, authentication via tokens, and data transmission, ensuring that only authorized clients can connect and interact with the server<br>- Additionally, it supports threading for concurrent operations.</td>
					</tr>
					<tr>
						<td><b><a href='https://github.com/eloicito333/dementia-assistant/blob/master/servers/websocket/requirements.txt'>requirements.txt</a></b></td>
						<td>- Specifies the dependencies required for the WebSocket server component of the project, ensuring compatibility and functionality across various libraries and frameworks<br>- It includes essential packages for web communication, data handling, and interface management, pivotal for the server's operation within the broader application architecture.</td>
					</tr>
					<tr>
						<td><b><a href='https://github.com/eloicito333/dementia-assistant/blob/master/servers/websocket/stream_handler.py'>stream_handler.py</a></b></td>
						<td>- StreamHandler manages real-time audio data processing for transcription in a WebSocket server environment<br>- It captures audio, determines speech presence, buffers it, and processes it through a transcription service<br>- The system handles dynamic buffer management and integrates user-specific prompts to enhance transcription context, ensuring efficient and continuous audio data handling and transcription output.</td>
					</tr>
					<tr>
						<td><b><a href='https://github.com/eloicito333/dementia-assistant/blob/master/servers/websocket/transcriber.py'>transcriber.py</a></b></td>
						<td>- Transcriber in the websocket server module automates voice transcription corrections for user messages, ensuring specific words and phrases are accurately represented and formatted according to predefined rules<br>- It leverages the OPENAI_CLIENT for generating corrected text outputs, enhancing clarity and adherence to stylistic guidelines.</td>
					</tr>
					<tr>
						<td><b><a href='https://github.com/eloicito333/dementia-assistant/blob/master/servers/websocket/essential_data.py'>essential_data.py</a></b></td>
						<td>- Defines essential data for the WebSocket server within the project, setting default user and assistant identities, including names and voice settings<br>- It also initializes a list for important words, likely used for processing or filtering content during WebSocket communications, enhancing interaction personalization and functionality across the system.</td>
					</tr>
					<tr>
						<td><b><a href='https://github.com/eloicito333/dementia-assistant/blob/master/servers/websocket/main_assistant.py'>main_assistant.py</a></b></td>
						<td>- Manages real-time interactions in a voice assistant designed to aid individuals with dementia, maintaining conversational context and handling user inputs<br>- It dynamically adjusts dialogue based on system prompts, user messages, and function calls, ensuring responses are tailored and relevant within the ongoing conversation.</td>
					</tr>
					<tr>
						<td><b><a href='https://github.com/eloicito333/dementia-assistant/blob/master/servers/websocket/auth.py'>auth.py</a></b></td>
						<td>- Authenticates WebSocket connections by verifying tokens against an environment-specified authorization token<br>- Located within the `servers/websocket` directory, `auth.py` ensures that only clients with the correct token can establish or maintain a connection, playing a critical role in securing the WebSocket server's communication channels.</td>
					</tr>
					<tr>
						<td><b><a href='https://github.com/eloicito333/dementia-assistant/blob/master/servers/websocket/player.py'>player.py</a></b></td>
						<td>- Manages audio playback and text-to-speech operations within a WebSocket server environment<br>- It handles audio streaming, temporary file management, and provides real-time audio control through threading<br>- The module integrates with an external AI client to generate speech from text, supporting dynamic interaction in applications requiring audio output.</td>
					</tr>
					</table>
					<details>
						<summary><b>utils</b></summary>
						<blockquote>
							<table>
							<tr>
								<td><b><a href='https://github.com/eloicito333/dementia-assistant/blob/master/servers/websocket/utils/objects.py'>objects.py</a></b></td>
								<td>- The `objects.py` module in the `servers/websocket/utils` directory provides functionality to safely retrieve elements from various data structures<br>- It supports accessing elements from dictionaries and other iterable types, handling non-existent keys and indices gracefully by returning a default value or the object itself under specific conditions.</td>
							</tr>
							<tr>
								<td><b><a href='https://github.com/eloicito333/dementia-assistant/blob/master/servers/websocket/utils/io.py'>io.py</a></b></td>
								<td>- Encodes and decodes data for efficient transmission over websockets within the project's architecture<br>- Utilizing msgpack serialization, the utility handles conversion of NumPy arrays to byte streams and vice versa, ensuring other data types are transmitted without alteration<br>- This process supports the seamless exchange of complex data structures necessary for real-time, data-intensive applications.</td>
							</tr>
							</table>
						</blockquote>
					</details>
					<details>
						<summary><b>function_calling</b></summary>
						<blockquote>
							<table>
							<tr>
								<td><b><a href='https://github.com/eloicito333/dementia-assistant/blob/master/servers/websocket/function_calling/get_tdr_conclusions.py'>get_tdr_conclusions.py</a></b></td>
								<td>- GetTDRConclusions, part of the websocket functionality in the codebase, provides conclusions for a given set of hypotheses about voice assistant capabilities and their applications, particularly in Catalan and for elderly autonomy<br>- It utilizes predefined responses to reflect on the verification of these hypotheses, enhancing user understanding of the technology's impact and feasibility.</td>
							</tr>
							<tr>
								<td><b><a href='https://github.com/eloicito333/dementia-assistant/blob/master/servers/websocket/function_calling/function_parent_class.py'>function_parent_class.py</a></b></td>
								<td>- Defines the `OpenAIFunction` class within the WebSocket server's architecture, serving as a parent class for function calling<br>- It outlines a structure for subclasses to implement specific functionalities, including a method to apply arguments and a static method to retrieve the function's name, enhancing modularity and reusability across the system.</td>
							</tr>
							<tr>
								<td><b><a href='https://github.com/eloicito333/dementia-assistant/blob/master/servers/websocket/function_calling/vector_data_retrieval.py'>vector_data_retrieval.py</a></b></td>
								<td>- VectorDataRetrieval, a component within the websocket server, facilitates historical context retrieval from conversational data<br>- It leverages an API to search through documented conversations based on text, date, and speaker parameters, returning relevant past dialogues<br>- This function supports contextual understanding across the application by accessing a vector database.</td>
							</tr>
							<tr>
								<td><b><a href='https://github.com/eloicito333/dementia-assistant/blob/master/servers/websocket/function_calling/function_handler.py'>function_handler.py</a></b></td>
								<td>- FunctionHandler orchestrates the execution of various server-side functions related to data retrieval, datetime operations, and reminder management within a WebSocket environment<br>- It maps function calls to specific handlers, executes them concurrently, and formats the results for WebSocket communication, enhancing the system's responsiveness and interactivity.</td>
							</tr>
							<tr>
								<td><b><a href='https://github.com/eloicito333/dementia-assistant/blob/master/servers/websocket/function_calling/get_current_datetime.py'>get_current_datetime.py</a></b></td>
								<td>- GetCurerntDatetime, part of the websocket server's function calling module, provides real-time date and time information<br>- It extends the OpenAIFunction class, offering a method to fetch the current weekday in Catalan and the complete date and time, enhancing user interaction by responding with natural language placeholders during processing.</td>
							</tr>
							</table>
							<details>
								<summary><b>reminders</b></summary>
								<blockquote>
									<table>
									<tr>
										<td><b><a href='https://github.com/eloicito333/dementia-assistant/blob/master/servers/websocket/function_calling/reminders/get_all.py'>get_all.py</a></b></td>
										<td>- GetAllReminders, a class within the websocket server's reminder management module, facilitates the retrieval of all existing reminders from the database<br>- It extends the OpenAIFunction parent class, incorporating predefined user interaction phrases and leveraging an API helper to access reminder data, thereby supporting comprehensive reminder management in the application.</td>
									</tr>
									<tr>
										<td><b><a href='https://github.com/eloicito333/dementia-assistant/blob/master/servers/websocket/function_calling/reminders/get_by_id.py'>get_by_id.py</a></b></td>
										<td>- GetReminderById, a component within the websocket server's reminder management system, retrieves existing reminders by their unique ID<br>- It utilizes the api_helper to interact with the reminders database, ensuring efficient data retrieval<br>- This functionality is crucial for enabling users to access specific reminder details within the broader application architecture.</td>
									</tr>
									<tr>
										<td><b><a href='https://github.com/eloicito333/dementia-assistant/blob/master/servers/websocket/function_calling/reminders/create.py'>create.py</a></b></td>
										<td>- CreateReminder, a component within the websocket functionality of the project, manages the creation of reminders<br>- It interfaces with an API to store reminder details such as frequency, title, and timing in a database<br>- This module ensures users are notified appropriately before a reminder is set, enhancing user interaction and reliability of the reminder system.</td>
									</tr>
									<tr>
										<td><b><a href='https://github.com/eloicito333/dementia-assistant/blob/master/servers/websocket/function_calling/reminders/update.py'>update.py</a></b></td>
										<td>- UpdateReminder, a class within the websocket server's reminder management module, facilitates the modification of existing reminders<br>- It allows users to specify which attributes of a reminder to update, such as frequency, title, and timing details, ensuring flexibility in managing scheduled notifications<br>- This functionality is crucial for maintaining the accuracy and relevance of reminder data in dynamic environments.</td>
									</tr>
									<tr>
										<td><b><a href='https://github.com/eloicito333/dementia-assistant/blob/master/servers/websocket/function_calling/reminders/delete.py'>delete.py</a></b></td>
										<td>- DeleteReminder, a class within the websocket server's reminder management module, facilitates the removal of existing reminders by interacting with the database through the api_helper<br>- It leverages a structured description to validate and process the deletion request based on the reminder's ID, ensuring efficient and accurate operations within the system's architecture.</td>
									</tr>
									</table>
								</blockquote>
							</details>
						</blockquote>
					</details>
				</blockquote>
			</details>
		</blockquote>
	</details>
	<details> <!-- client Submodule -->
		<summary><b>client</b></summary>
		<blockquote>
			<table>
			<tr>
				<td><b><a href='https://github.com/eloicito333/dementia-assistant/blob/master/client/program_settings.py'>program_settings.py</a></b></td>
				<td>- Manages user preferences within the client module by setting program behavior flags, specifically controlling output verbosity and deletion operations<br>- By enabling verbose output and disabling the delete function, it ensures comprehensive feedback and data preservation during program execution, aligning with the broader codebase's focus on robustness and user control.</td>
			</tr>
			<tr>
				<td><b><a href='https://github.com/eloicito333/dementia-assistant/blob/master/client/client.py'>client.py</a></b></td>
				<td>- Client.py establishes a WebSocket client that connects to a server, handling audio data transmission<br>- It encodes audio arrays and voice presence flags, sends them to the server, and processes the received responses<br>- The client utilizes environment variables for configuration and leverages threading to manage WebSocket communication efficiently.</td>
			</tr>
			<tr>
				<td><b><a href='https://github.com/eloicito333/dementia-assistant/blob/master/client/stream_constants.py'>stream_constants.py</a></b></td>
				<td>- Defines constants crucial for managing audio stream parameters within the client module, including frequency ranges for vocal detection, sample rate compatibility with external APIs, and block sizes for processing audio data<br>- These settings ensure efficient audio data handling and synchronization across the system's audio processing and transmission functionalities.</td>
			</tr>
			<tr>
				<td><b><a href='https://github.com/eloicito333/dementia-assistant/blob/master/client/.env.demo'>.env.demo</a></b></td>
				<td>- Serves as a template for environment variables in the client application, specifying the WebSocket URL and authentication token necessary for connecting to the server<br>- Essential for developers to configure their local development environments correctly, ensuring seamless communication and authentication with the backend services.</td>
			</tr>
			<tr>
				<td><b><a href='https://github.com/eloicito333/dementia-assistant/blob/master/client/main.py'>main.py</a></b></td>
				<td>- Client/main.py serves as the entry point for a voice assistant application, initializing the audio player and stream handler to manage audio input and output<br>- It configures user interaction settings like verbose and no-delete modes, and displays a welcome message, enhancing user experience by providing feedback on current operational modes.</td>
			</tr>
			<tr>
				<td><b><a href='https://github.com/eloicito333/dementia-assistant/blob/master/client/requirements.txt'>requirements.txt</a></b></td>
				<td>- Defines the specific Python package dependencies required for the client component of the project, ensuring compatibility and functionality across various modules<br>- It includes libraries for data manipulation, network communication, and environmental settings, crucial for the client's operational integrity and interaction with other services.</td>
			</tr>
			<tr>
				<td><b><a href='https://github.com/eloicito333/dementia-assistant/blob/master/client/stream_handler.py'>stream_handler.py</a></b></td>
				<td>- StreamHandler manages audio streams for real-time voice processing, handling tasks such as voice detection, audio buffering, and transcription initiation<br>- It integrates with the system's audio devices, supports echo cancellation in contaminated streams, and processes audio data to facilitate continuous speech recognition and response within an interactive AI assistant environment.</td>
			</tr>
			<tr>
				<td><b><a href='https://github.com/eloicito333/dementia-assistant/blob/master/client/essential_data.py'>essential_data.py</a></b></td>
				<td>- Defines essential user and assistant attributes for the client module within the broader application architecture<br>- It sets basic identity parameters such as names and voice preferences, crucial for personalizing interactions<br>- The module also includes a placeholder for important words, suggesting a foundation for future feature expansions involving tailored communication or keyword-based functionalities.</td>
			</tr>
			<tr>
				<td><b><a href='https://github.com/eloicito333/dementia-assistant/blob/master/client/player.py'>player.py</a></b></td>
				<td>- AudioPlayer, defined in client/player.py, manages audio output for the system<br>- It initializes an output buffer and queue, receives audio blocks via a socket connection, and supports stopping the audio stream on command<br>- The class leverages threading to handle stop operations without blocking the main execution flow.</td>
			</tr>
			</table>
			<details>
				<summary><b>utils</b></summary>
				<blockquote>
					<table>
					<tr>
						<td><b><a href='https://github.com/eloicito333/dementia-assistant/blob/master/client/utils/objects.py'>objects.py</a></b></td>
						<td>- `client/utils/objects.py` provides a utility function for safely accessing elements within various data structures<br>- It supports dictionaries, iterables, and handles non-subscriptable objects by returning defaults or the object itself based on the provided key<br>- This enhances data handling robustness across the client-side architecture of the application.</td>
					</tr>
					<tr>
						<td><b><a href='https://github.com/eloicito333/dementia-assistant/blob/master/client/utils/io.py'>io.py</a></b></td>
						<td>- Handles the serialization and deserialization of data for network transmission within the client module, specifically adapting NumPy arrays for efficient byte stream conversion using msgpack<br>- It ensures that complex data structures are appropriately encoded and decoded, maintaining integrity and type consistency across network interactions.</td>
					</tr>
					</table>
				</blockquote>
			</details>
		</blockquote>
	</details>
</details>

---
## 🚀 Getting Started

### ☑️ Prerequisites

Before getting started with dementia-assistant, ensure your runtime environment meets the following requirements:

- **Programming Language:** Python
- **Package Manager:** Npm, Pip


### ⚙️ Installation

Install dementia-assistant using one of the following methods:

**Build from source:**

1. Clone the dementia-assistant repository:
```sh
❯ git clone https://github.com/eloicito333/dementia-assistant
```

2. Navigate to the project directory:
```sh
❯ cd dementia-assistant
```

3. Install the project dependencies:


**Using `npm`** &nbsp; [<img align="center" src="" />]()

```sh
❯ echo 'INSERT-INSTALL-COMMAND-HERE'
```


**Using `pip`** &nbsp; [<img align="center" src="https://img.shields.io/badge/Pip-3776AB.svg?style={badge_style}&logo=pypi&logoColor=white" />](https://pypi.org/project/pip/)

```sh
❯ pip install -r servers/websocket/requirements.txt, client/requirements.txt
```




### 🤖 Usage
Run dementia-assistant using the following command:
**Using `npm`** &nbsp; [<img align="center" src="" />]()

```sh
❯ echo 'INSERT-RUN-COMMAND-HERE'
```


**Using `pip`** &nbsp; [<img align="center" src="https://img.shields.io/badge/Pip-3776AB.svg?style={badge_style}&logo=pypi&logoColor=white" />](https://pypi.org/project/pip/)

```sh
❯ python {entrypoint}
```


### 🧪 Testing
Run the test suite using the following command:
**Using `npm`** &nbsp; [<img align="center" src="" />]()

```sh
❯ echo 'INSERT-TEST-COMMAND-HERE'
```


**Using `pip`** &nbsp; [<img align="center" src="https://img.shields.io/badge/Pip-3776AB.svg?style={badge_style}&logo=pypi&logoColor=white" />](https://pypi.org/project/pip/)

```sh
❯ pytest
```


---
## 📌 Project Roadmap

- [X] **`Task 1`**: <strike>Implement feature one.</strike>
- [ ] **`Task 2`**: Implement feature two.
- [ ] **`Task 3`**: Implement feature three.

---

## 🔰 Contributing

- **💬 [Join the Discussions](https://github.com/eloicito333/dementia-assistant/discussions)**: Share your insights, provide feedback, or ask questions.
- **🐛 [Report Issues](https://github.com/eloicito333/dementia-assistant/issues)**: Submit bugs found or log feature requests for the `dementia-assistant` project.
- **💡 [Submit Pull Requests](https://github.com/eloicito333/dementia-assistant/blob/main/CONTRIBUTING.md)**: Review open PRs, and submit your own PRs.

<details closed>
<summary>Contributing Guidelines</summary>

1. **Fork the Repository**: Start by forking the project repository to your github account.
2. **Clone Locally**: Clone the forked repository to your local machine using a git client.
   ```sh
   git clone https://github.com/eloicito333/dementia-assistant
   ```
3. **Create a New Branch**: Always work on a new branch, giving it a descriptive name.
   ```sh
   git checkout -b new-feature-x
   ```
4. **Make Your Changes**: Develop and test your changes locally.
5. **Commit Your Changes**: Commit with a clear message describing your updates.
   ```sh
   git commit -m 'Implemented new feature x.'
   ```
6. **Push to github**: Push the changes to your forked repository.
   ```sh
   git push origin new-feature-x
   ```
7. **Submit a Pull Request**: Create a PR against the original project repository. Clearly describe the changes and their motivations.
8. **Review**: Once your PR is reviewed and approved, it will be merged into the main branch. Congratulations on your contribution!
</details>

<details closed>
<summary>Contributor Graph</summary>
<br>
<p align="left">
   <a href="https://github.com{/eloicito333/dementia-assistant/}graphs/contributors">
      <img src="https://contrib.rocks/image?repo=eloicito333/dementia-assistant">
   </a>
</p>
</details>

---

## 🎗 License

This project is protected under the [SELECT-A-LICENSE](https://choosealicense.com/licenses) License. For more details, refer to the [LICENSE](https://choosealicense.com/licenses/) file.

---

## 🙌 Acknowledgments

- List any resources, contributors, inspiration, etc. here.

---