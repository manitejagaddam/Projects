
import './App.css'

function App() {


  return (
    
      <div className="w-full h-screen bg-zinc-600 ">

      
      
      <h1 className='text-6xl text-center p-10'> Password Generator</h1>
      <div className="input flex flex-col align-middle justify-center w-50">

      <input type="text" className='w-56 ' />
      <div className="buttons flex gap-4 justify-center">
        <input type="range" name="" id="" /><span className='text-xl'>Length</span>
        <input type="checkbox" name="" id="" /><span className='text-xl'>Alphabets</span>
        <input type="checkbox" name="" id="" /><span className='text-xl'>Number</span>
        <input type="checkbox" name="" id="" /><span className='text-xl'>Symbols</span>
      </div>
      
      </div>


      </div>
    
  )
}

export default App
