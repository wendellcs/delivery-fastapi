import { useEffect, useState } from "react";

function App() {
  const [tarefa, setTarefa] = useState("");
  const [tarefas, setTarefas] = useState([]);

  function adicionar() {
    if (tarefa === "") return;

    setTarefas([...tarefas, tarefa]);
    setTarefa("");
  }

  function remover(index) {
    setTarefas(tarefas.filter((_, i) => i !== index));
  }

  useEffect(() => {
    console.log("Tarefas:", tarefas);
  }, [tarefas]);

  return (
    <div>
      <h1>Lista de Tarefas</h1>

      <input
        value={tarefa}
        onChange={(e) => setTarefa(e.target.value)}
      />

      <button onClick={adicionar}>Adicionar</button>

      <ul>
        {tarefas.map((tarefa, index) => (
          <li key={index}>
            {tarefa}

            <button onClick={() => remover(index)}>
              Remover
            </button>
          </li>
        ))}
      </ul>
    </div>
  );
}

export default App;