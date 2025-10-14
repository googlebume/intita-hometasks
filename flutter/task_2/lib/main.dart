import 'package:flutter/cupertino.dart';
import 'package:flutter/material.dart';
import 'package:flutter_bloc/flutter_bloc.dart';
import 'package:task_2/classes/calculator_block.dart';
import 'package:task_2/secondScreen.dart';


void main() {
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Flutter Demo',
      home: BlocProvider(
        create: (context) => CalculatorBloc(),
        child: MyHomePage(),
      ),
    );
  }
}

class MyHomePage extends StatefulWidget {
  MyHomePage({super.key});

  @override
  State<StatefulWidget> createState() {
    return _MyHomePageState();
  }
}

class _MyHomePageState extends State<MyHomePage> {
  var currentColor = 0;
  var colors = [Colors.orange, Colors.blueAccent, Colors.green, Colors.amber];
  String? inputFromSecondScreen;

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: [
            Container(
              alignment: Alignment.center,
              color: colors[currentColor],
              width: 300,
              height: 200,
            ),
            const SizedBox(height: 20),
            CupertinoButton(
              child: const Text('Change Color'),
              onPressed: () {
                setState(() {
                  if (currentColor >= colors.length - 1) {
                    currentColor = 0;
                    return;
                  }
                  currentColor += 1;
                });
              },
            ),
            const SizedBox(height: 30),
            BlocBuilder<CalculatorBloc, CalculatorState>(
              builder: (context, state) {
                return Text(state.displayText.toString());
              },
            ),
            const SizedBox(height: 20),
            Column(
              children: [
                Row(
                  mainAxisAlignment: MainAxisAlignment.center,
                  children: [
                    ElevatedButton(
                        onPressed: () => context
                            .read<CalculatorBloc>()
                            .add(NumberPressedEvent(1)),
                        child: const Text('1')),
                    const SizedBox(width: 10),
                    ElevatedButton(
                        onPressed: () => context
                            .read<CalculatorBloc>()
                            .add(NumberPressedEvent(2)),
                        child: const Text('2')),
                    const SizedBox(width: 10),
                    ElevatedButton(
                        onPressed: () => context
                            .read<CalculatorBloc>()
                            .add(NumberPressedEvent(3)),
                        child: const Text('3')),
                  ],
                ),
                const SizedBox(height: 10),
                Row(
                  mainAxisAlignment: MainAxisAlignment.center,
                  children: [
                    ElevatedButton(
                        onPressed: () => context
                            .read<CalculatorBloc>()
                            .add(NumberPressedEvent(4)),
                        child: const Text('4')),
                    const SizedBox(width: 10),
                    ElevatedButton(
                        onPressed: () => context
                            .read<CalculatorBloc>()
                            .add(NumberPressedEvent(5)),
                        child: const Text('5')),
                    const SizedBox(width: 10),
                    ElevatedButton(
                        onPressed: () => context
                            .read<CalculatorBloc>()
                            .add(NumberPressedEvent(6)),
                        child: const Text('6')),
                  ],
                ),
                const SizedBox(height: 10),
                Row(
                  mainAxisAlignment: MainAxisAlignment.center,
                  children: [
                    ElevatedButton(
                        onPressed: () => context
                            .read<CalculatorBloc>()
                            .add(NumberPressedEvent(7)),
                        child: const Text('7')),
                    const SizedBox(width: 10),
                    ElevatedButton(
                        onPressed: () => context
                            .read<CalculatorBloc>()
                            .add(NumberPressedEvent(8)),
                        child: const Text('8')),
                    const SizedBox(width: 10),
                    ElevatedButton(
                        onPressed: () => context
                            .read<CalculatorBloc>()
                            .add(NumberPressedEvent(9)),
                        child: const Text('9')),
                  ],
                ),
                const SizedBox(height: 10),
                ElevatedButton(
                    onPressed: () => context
                        .read<CalculatorBloc>()
                        .add(ClearPressedEvent()),
                    child: const Text('Clear')),
                const SizedBox(height: 30),
                ElevatedButton(
                  onPressed: () async {
                    final result = await Navigator.push(
                      context,
                      MaterialPageRoute(
                          builder: (context) => const SecondScreen()),
                    );
                    if (result != null) {
                      setState(() {
                        inputFromSecondScreen = result as String;
                      });
                    }
                  },
                  child: const Text("Go to Second Screen"),
                ),
                Text(inputFromSecondScreen ?? "Empty"),
              ],
            ),
          ],
        ),
      ),
    );
  }
}