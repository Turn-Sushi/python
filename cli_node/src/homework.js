import { Command } from 'commander';
import { list, insert, remove, update } from './words.js'; 

const program = new Command();

program
    .command('list')
    .action(list)

program
    .command('insert')
    .argument('<word>')
    .action(insert)

program
    .command('remove')
    .argument('<id>')
    .action(remove)

program
    .command('update')
    .argument('<id>')
    .argument('<word>')
    .action(update)
    
program.parse(process.argv);